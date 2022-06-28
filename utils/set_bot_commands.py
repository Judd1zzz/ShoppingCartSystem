from aiogram import types


# function for creating custom commands
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "📖 Launch the bot"),
        types.BotCommand("shop", "🛍 Shop"),
        types.BotCommand("cart", "🛒 Cart"),
    ])
