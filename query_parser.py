"""Визначає, що ввів користувач: VIN-код, номерний знак чи щось незрозуміле."""

import re
from enum import Enum

# Кириличні літери, які на номерах виглядають так само, як латинські.
# Українські номери використовують лише ці 12 літер: А В С Е Н І К М О Р Т Х.
CYRILLIC_TO_LATIN = str.maketrans("АВСЕНІКМОРТХ", "ABCEHIKMOPTX")

# VIN: рівно 17 символів, латинські літери та цифри, крім I, O, Q
# (їх не використовують, щоб не плутати з 1 і 0).
VIN_PATTERN = re.compile(r"[A-HJ-NPR-Z0-9]{17}")

# Український номер нового зразка: 2 літери, 4 цифри, 2 літери (наприклад AA1234BB).
PLATE_PATTERN = re.compile(r"[ABCEHIKMOPTX]{2}\d{4}[ABCEHIKMOPTX]{2}")


class QueryType(Enum):
    VIN = "vin"
    PLATE = "plate"
    UNKNOWN = "unknown"


def normalize(text: str) -> str:
    """Прибирає пробіли й дефіси, робить великі літери, кирилицю замінює на латиницю."""
    cleaned = re.sub(r"[\s\-]", "", text).upper()
    return cleaned.translate(CYRILLIC_TO_LATIN)


def detect_query_type(text: str) -> tuple[QueryType, str]:
    """Повертає тип запиту та нормалізований текст, за яким потім шукати в даних."""
    query = normalize(text)

    if VIN_PATTERN.fullmatch(query):
        return QueryType.VIN, query
    if PLATE_PATTERN.fullmatch(query):
        return QueryType.PLATE, query
    return QueryType.UNKNOWN, query
