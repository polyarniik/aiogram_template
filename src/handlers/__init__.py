from aiogram import Dispatcher

from src.handlers import admin, user, error


def setup(dp: Dispatcher):
    admin.setup(dp)
    error.setup(dp)
    user.setup(dp)
