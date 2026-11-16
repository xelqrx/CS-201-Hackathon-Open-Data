"""Пошук автівки у відкритих даних.

Бот викликає лише ці дві функції, тож змінювати bot.py не доведеться.
"""

import os
from functools import lru_cache
from html import escape

from sqlalchemy import URL, create_engine, select
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.engine import Engine
from sqlalchemy.sql import Select

from classes.cars_number import Number
from classes.data import DataClean


@lru_cache(maxsize=1) # створюється одна сесія підключення до бд під час роботи бота, яка зберігає максимум 1 запит в кеші
def _get_engine() -> Engine:
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    if not host or not port or not username or not password or not database:
        missing = [
            name
            for name, value in (
                ("DB_HOST", host),
                ("DB_PORT", port),
                ("DB_USER", username),
                ("DB_PASSWORD", password),
                ("DB_NAME", database),
            )
            if not value
        ]
        raise RuntimeError(
            "Не задано параметри підключення до бази даних: "
            + ", ".join(missing)
        )

    try:
        port_number = int(port)
    except ValueError as error:
        raise RuntimeError("DB_PORT має бути числом") from error

    return create_engine(
        URL.create(
            "postgresql+psycopg",
            username=username,
            password=password,
            host=host,
            port=port_number,
            database=database,
        )
    )


def _format_car(car: DataClean) -> str:
    details = [
        ("Марка", car.brand.brand if car.brand else None),
        ("Модель", car.model.model if car.model else None),
        ("Рік випуску", car.make_year),
        ("Номерний знак", car.car_number.number if car.car_number else None),
        ("Колір", car.color.color if car.color else None),
        ("Тип кузова", car.body.body if car.body else None),
        ("Паливо", car.fuel.fuel if car.fuel else None),
        ("VIN", car.vin),
    ]
    return "\n".join(
        f"<b>{label}:</b> {escape(str(value))}"
        for label, value in details
        if value
    )


def _find_car(statement: Select[tuple[DataClean]]) -> str | None:
    statement = statement.order_by(DataClean.id.desc()).options(
        joinedload(DataClean.brand),
        joinedload(DataClean.model),
        joinedload(DataClean.car_number),
        joinedload(DataClean.color),
        joinedload(DataClean.body),
        joinedload(DataClean.fuel),
    )
    with Session(_get_engine()) as session:
        car = session.scalars(statement).first()
        return _format_car(car) if car is not None else None


def find_by_vin(vin: str) -> str | None:
    """Повертає опис автівки за VIN або None, якщо нічого не знайдено."""
    return _find_car(select(DataClean).where(DataClean.vin == vin))


def find_by_plate(plate: str) -> str | None:
    """Повертає опис автівки за номерним знаком або None, якщо нічого не знайдено."""
    statement = (
        select(DataClean)
        .join(DataClean.car_number)
        .where(Number.number == plate)
    )
    return _find_car(statement)
