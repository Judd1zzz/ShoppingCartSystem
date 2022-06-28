from aiogram import Dispatcher
from .user import UserFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(UserFilter)
