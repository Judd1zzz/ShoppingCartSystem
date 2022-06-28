from loader import dp
from aiogram.types import Message
from utils.db_api.sqlite3 import SQLite
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Command
from keyboards.default.main_menu import main_menu
from keyboards.inline.inline import choose_categories_inline


# Handler of the '🛍 Shop' message or the 'shop' command
@dp.message_handler(Text(equals='🛍 Shop') | Command('shop'))
async def show_cart(message: Message):
    user_id = message.from_user.id
    match SQLite(user_id=user_id).check_categories:  # <--- Checking for the presence of categories in the database
        case None:
            await message.answer('<strong>❗️ Unfortunately, there are no products</strong>',
                                 reply_markup=await main_menu())
        case _:
            await message.answer('Choose the category that suits you ⬇️', reply_markup=await choose_categories_inline())
