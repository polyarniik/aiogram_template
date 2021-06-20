import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from .config import BOT_TOKEN


bot = aiogram.Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

# You can use other repositories described in the current aiogram documentation
storage = MemoryStorage()

# Dispather is designed to catch all requests sent to the bot
dp = aiogram.Dispatcher(bot, storage=storage)
