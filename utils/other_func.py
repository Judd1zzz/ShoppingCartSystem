# - *- coding: utf- 8 - *-
from loader import bot, admin_ids


# Notification when running the script
async def on_startup_notify():
    if len(admin_ids) < 1:
        print("******** You did not specify the administrator ID ********")
    elif len(admin_ids) >= 1:
        notify = f"<strong>✅ The bot was successfully launched</strong>\n"
        await send_all_admin(notify)


# Sending a message to all administrators
async def send_all_admin(message, markup=None, not_me=0):
    if markup is None:
        for admin in admin_ids:
            try:
                if str(admin) != str(not_me):
                    await bot.send_message(admin, message, disable_web_page_preview=True)
            except:
                pass
    else:
        for admin in admin_ids:
            try:
                if str(admin) != str(not_me):
                    await bot.send_message(admin, message, reply_markup=markup, disable_web_page_preview=True)
            except:
                pass

