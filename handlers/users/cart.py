from loader import dp
from aiogram.types import Message
from utils.db_api.sqlite3 import SQLite
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Command
from keyboards.default.main_menu import main_menu
from keyboards.inline.inline import go_to_payment_inline


# Handler of the '🛒 Cart' message or 'cart' command
@dp.message_handler(Text(equals='🛒 Cart') | Command('cart'))
async def show_cart(message: Message):
    user_id = message.from_user.id
    match SQLite(user_id=user_id).check_user_cart:  # <--- checking for the availability of products in the user's cart
        case None:
            await message.answer('<strong>❗️ Your shopping cart is empty</strong>',
                                 reply_markup=await main_menu())
        case _:
            msg = f'<strong>Products that are in your cart</strong>\n'
            func = SQLite(user_id=user_id)
            info = func.select_user_cart
            total_price = 0
            for a in range(len(info)):  # <--- creating a message in the format we need
                func = SQLite(position_id=info[a][1])
                name = func.select_position.name
                price = func.select_position.price
                total_price += price
                msg += f'<strong>Product</strong>: <code>{name}</code> - <code>{format(price, ",d").replace(",", ".")}₽</code>\n'
            msg += f'<strong>Total amount</strong>: <code>{format(total_price, ",d").replace(",", ".")}₽</code>'
            await message.answer(msg, reply_markup=await go_to_payment_inline(user_id=user_id))