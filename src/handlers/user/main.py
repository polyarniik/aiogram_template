from aiogram.types import Message

from config.loader import bot


async def start(message: Message):
    await bot.send_message(message.from_user.id, "Привет!")
