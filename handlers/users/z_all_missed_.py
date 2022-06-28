# - *- coding: utf- 8 - *-
from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageCantBeDeleted


# Processing of all callbacks that have lost states after restarting the script
@dp.callback_query_handler(text="...", state="*")
async def processing_missed_callback(call: CallbackQuery, state: FSMContext):
    await call.answer()


# Processing of all callbacks that have lost statuses after restarting the script
@dp.callback_query_handler(state="*")
async def processing_missed_callback(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except MessageCantBeDeleted:
        pass
    await call.message.answer("<strong>❗ An error occurred in data processing</strong>\n"
                              "📋 It is possible that your data was not found due to restarting the script.\n"
                              "⚙️ Try to perform the action again or contact technical support.")


# Processing all unknown messages
@dp.message_handler()
async def processing_missed_messages(message: types.Message):
    await message.answer("<strong>♦ Unknown command</strong>\n")
