"""Telegram-бот: за VIN-кодом або номерним знаком розповідає, що це за автівка."""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from car_search import find_by_plate, find_by_vin
from query_parser import QueryType, detect_query_type

START_TEXT = (
    "Привіт! Надішли мені VIN-код або номерний знак автівки, "
    "і я розповім, що це за машина.\n\n"
    "Приклади:\n"
    "• VIN: <code>WVWZZZ1KZAW000001</code>\n"
    "• Номер: <code>AA1234BB</code>"
)

UNKNOWN_TEXT = (
    "Це не схоже ні на VIN-код, ні на номерний знак 🤔\n\n"
    "• VIN має 17 символів: латинські літери (крім I, O, Q) та цифри.\n"
    "• Номер має формат <code>AA1234BB</code>: 2 літери, 4 цифри, 2 літери."
)

NOT_FOUND_TEXT = "Нічого не знайшов за запитом <code>{query}</code> 😕"

dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def handle_start(message: Message) -> None:
    await message.answer(START_TEXT)


@dispatcher.message(F.text)
async def handle_query(message: Message) -> None:
    query_type, query = detect_query_type(message.text)

    if query_type is QueryType.UNKNOWN:
        await message.answer(UNKNOWN_TEXT)
        return

    if query_type is QueryType.VIN:
        result = find_by_vin(query)
    else:
        result = find_by_plate(query)

    if result is None:
        await message.answer(NOT_FOUND_TEXT.format(query=query))
    else:
        await message.answer(result)


@dispatcher.message()
async def handle_other(message: Message) -> None:
    """Відповідь на стікери, фото тощо — бот розуміє лише текст."""
    await message.answer("Надішли, будь ласка, VIN-код або номер текстом.")


async def main() -> None:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Не знайдено BOT_TOKEN. Додай його у файл .env")

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode="HTML"))
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
