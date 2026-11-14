
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Не найден токен Telegram-бота в файле .env")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Здравствуйте! Я — консультационный помощник ХГПУ.\n\n"
        "Задайте свой вопрос, и я постараюсь найти ответ "
        "в базе консультаций."
    )


@dp.message()
async def process_message(message: Message):
    await message.answer(
        "Ваше сообщение получено. Поиск ответа будет доступен "
        "после подключения базы 1С."
    )


async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
