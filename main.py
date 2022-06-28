import asyncio
from handlers import dp
from utils import create_all
from loader import bot, config
from utils.other_func import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def main():
    bot['config'] = config

    print('Bot was started')
    await on_startup_notify()
    await set_default_commands(dp)
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        create_all()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
