from utils.db_api.sqlite3 import SQLite
from loader import dp, bot, payments_token
from aiogram.types.message import ContentType
from keyboards.inline.callback_datas import *
from keyboards.default.main_menu import main_menu
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message
from keyboards.inline.inline import choose_categories_inline, choose_positions_inline, add_to_cart_inline


# Handler for pressing an inline button with the category name
@dp.callback_query_handler(choose_category.filter(type='choose_category') | back_to_positions.filter(type='back_to_positions'))
async def on_selecting_category(call: CallbackQuery, callback_data: dict):
    await call.answer()
    category_id = callback_data.get('category_id')
    func = SQLite(category_id=category_id)
    count_positions = len(func.select_all_positions)
    category_name = func.select_category.name
    if count_positions < 1:
        await call.message.edit_text('<strong>❗️ Unfortunately, there are no products in this category yet</strong>')
    else:
        await call.message.edit_text(f'<strong>Selected category</strong>: <code>{category_name}</code>', 
                                    reply_markup=await choose_positions_inline(category_id))


# Handler for pressing an inline button to return to the selection of categories
@dp.callback_query_handler(back_to_categories.filter(type='back_to_categories'))
async def back_to_categories(call: CallbackQuery):
    await call.answer()
    user_id = call.from_user.id
    match SQLite(user_id=user_id).check_categories:
        case None:
            await call.message.edit_text('<strong>❗️ Unfortunately, there are no products</strong>',
                                 reply_markup=await main_menu())
        case _:
            await call.message.edit_text('Choose the category that suits you ⬇️', reply_markup=await choose_categories_inline())


# Handler for pressing an inline button to display position info
@dp.callback_query_handler(choose_position.filter(type='choose_position'))
async def on_selecting_position(call: CallbackQuery, callback_data: dict):
    await call.answer()
    user_id = call.from_user.id
    category_id = callback_data.get('category_id')
    position_id = callback_data.get('position_id')
    func = SQLite(category_id=category_id, position_id=position_id)
    category_name = func.select_category.name
    position_name = func.select_position.name
    position_price = func.select_position.price
    msg = f'🗂 <code>{category_name}/{position_name}</code>\n\n' \
          f'📍 Selected product: <code>{func.select_position.name}</code>\n' \
          f'💵 Price: <code>{format(position_price, ",d").replace(",", ".")}₽</code>\n'
    await call.message.edit_text(msg, reply_markup=await add_to_cart_inline(user_id=user_id, position_id=position_id))


# Handler for pressing the inline button "🛒 Add to cart"
@dp.callback_query_handler(add_to_cart.filter(type='add_to_cart'))
async def on_push_add_to_cart(call: CallbackQuery, callback_data: dict):
    await call.answer()
    user_id = call.from_user.id
    position_id = callback_data.get('position_id')
    SQLite(user_id=user_id, position_id=position_id).add_to_cart
    await call.message.edit_text('✅ The product was successfully added to the cart')


# Handler for pressing the inline button "💨 Clear cart"
@dp.callback_query_handler(clear_cart.filter(type='clear_cart'))
async def on_push_add_to_cart(call: CallbackQuery):
    await call.answer()
    user_id = call.from_user.id
    SQLite(user_id=user_id).delete_user_cart
    await call.message.edit_text('✅ The trash was successfully emptied')


# Handler for pressing the inline button "💳 Go to payment"
@dp.callback_query_handler(go_to_payment.filter(type='go_to_payment'))
async def on_push_add_to_cart(call: CallbackQuery, callback_data: dict):
    await call.answer()
    user_id = callback_data.get('user_id')
    data = SQLite(user_id=user_id).select_user_cart
    new_data =[]
    for i in range(len(data)):
        new_data.append(SQLite(position_id=data[i][1]).select_position)
    new_data = [new_data[i] for i in range(len(new_data))]
    prices = [LabeledPrice(label=i[0], amount=int(f'{i[1]}00')) for i in new_data]
    await bot.send_invoice(
        user_id,
        title='Cart',
        description='Description',
        provider_token=payments_token,
        currency='rub',
        prices=prices,
        start_parameter='example',
        payload='some_invoice'
        )
    await call.message.edit_text('✅ The product was successfully added to the cart')


@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def s_pay(message: Message):
    user_id = message.chat.id
    SQLite(user_id=user_id).delete_user_cart
    await bot.send_message(user_id, '✅ The payment was successful')
