from aiogram.utils.callback_data import CallbackData


# All callback dates for using inline buttons
# ---------------------------------------------------------------------------------
choose_category = CallbackData('choose_category', 'category_id', 'type')
choose_position = CallbackData('choos_position', 'category_id', 'position_id', 'type')
add_to_cart = CallbackData('add_to_cart', 'user_id', 'position_id', 'type')
go_to_payment = CallbackData('add_to_cart', 'user_id', 'type')
clear_cart = CallbackData('add_to_cart', 'user_id', 'type')
back_to_categories = CallbackData('back_to_categories', 'type')
back_to_positions = CallbackData('back_to_categories', 'category_id', 'type')
# ---------------------------------------------------------------------------------
