from utils.db_api.sqlite3 import SQLite
from keyboards.inline.callback_datas import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Creating an inline keyboard with categories names
async def choose_categories_inline(remover: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    categories = SQLite().select_all_categories
    for a in range(remover, len(categories)):
        category_id = categories[a][0]
        category_name = categories[a][1]
        keyboard.add(InlineKeyboardButton(text=f"{category_name}",
                                          callback_data=choose_category.new(
                                            category_id=category_id, type='choose_category'
                                            )))
    return keyboard


# Creating an inline keyboard with positions names
async def choose_positions_inline(category_id: int, remover: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    positions = SQLite(category_id=category_id).select_all_positions
    for a in range(remover, len(positions)):
        position_name = positions[a][0]
        position_price = positions[a][1]
        position_id = positions[a][2]
        keyboard.add(InlineKeyboardButton(text=f'{position_name}: {format(position_price, ",d").replace(",", ".")}₽',
                                          callback_data=choose_position.new(
                                            category_id=category_id,
                                            position_id=position_id,
                                            type='choose_position'
                                            )))
    back_kb = InlineKeyboardButton(text=f"⬅️ Back ↩️",
                                          callback_data=back_to_categories.new(
                                            type='back_to_categories'
                                            ))
    keyboard.add(back_kb)
    return keyboard


# Creating an inline keyboard with the buttons '🛒 Add to cart' to add a position to the cart and '⬅️ Back ↩️' to return to the position selection menu
async def add_to_cart_inline(user_id: int, position_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    add_to_cart_kb = InlineKeyboardButton(text='🛒 Add to cart',
                                          callback_data=add_to_cart.new(
                                          user_id=user_id,
                                          position_id=position_id,
                                          type='add_to_cart'
                                          ))
    
    back_kb = InlineKeyboardButton(text=f"⬅️ Back ↩️",
                                        callback_data=back_to_positions.new(
                                        category_id=(SQLite(position_id=position_id).select_position.category_id),
                                        type='back_to_positions'
                                        ))
    keyboard.add(add_to_cart_kb)
    keyboard.add(back_kb)
    return keyboard


# Creating an inline keyboard with the buttons '💳 Go to payment' to create a payment and '💨 Clear cart' to clear the cart
async def go_to_payment_inline(user_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    go_to_payment_kb = InlineKeyboardButton(text='💳 Go to payment',
                                          callback_data=go_to_payment.new(
                                          user_id=user_id,
                                          type='go_to_payment'
                                          ))
    clear_cart_kb = InlineKeyboardButton(text='💨 Clear cart',
                                          callback_data=clear_cart.new(
                                          user_id=user_id,
                                          type='clear_cart'
                                          ))
    keyboard.add(go_to_payment_kb, clear_cart_kb)
    return keyboard
