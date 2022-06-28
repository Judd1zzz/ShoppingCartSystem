# - *- coding: utf- 8 - *-
from data.config import load_config
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


config = load_config(".env").tg_bot
storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
admin_ids = config.admin_ids
payments_token = config.payments_token
dp = Dispatcher(bot, storage=storage)
