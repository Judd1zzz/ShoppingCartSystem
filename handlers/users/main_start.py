from loader import dp
from aiogram import types
from filters import UserFilter
from keyboards import main_menu
from utils.db_api.sqlite3 import SQLite
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart


# Processing the '/start' command for unregistered users
@dp.message_handler(CommandStart(), UserFilter(is_reg=False), state="*")
async def start_unregister_users(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    user_name = message.from_user.username
    SQLite(user_id=user_id, user_name=user_name).add_user
    await message.answer('✅ You have successfully registered', reply_markup=await main_menu())


# Processing of all handlers with verification of user registration
@dp.message_handler(UserFilter(is_reg=False), state="*")
@dp.callback_query_handler(UserFilter(is_reg=False), state="*")
async def send_user_message(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<strong>❗ Your profile was not found.</strong>\n"
                         "▶ Enter /start")


# Processing the '/start' command for registered users
@dp.message_handler(CommandStart())
async def start_register_users(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Hello, user!', reply_markup=await main_menu())
