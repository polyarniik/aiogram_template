from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

import handlers.user.main as mh


def setup(dp: Dispatcher):
    print("setup user")
    dp.register_message_handler(mh.start, CommandStart())
