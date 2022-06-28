from aiogram.types import ReplyKeyboardMarkup


# Basic buttons for using the bot
async def main_menu():
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("🛍 Shop", "🛒 Cart")
    return menu_default
