import typing
from loader import admin_ids
from utils.db_api.sqlite3 import SQLite
from aiogram.dispatcher.filters import BoundFilter


# Universal filter for various user checks
class UserFilter(BoundFilter):
    key = ['is_reg', 'is_admin']

    # Initializing input data
    def __init__(self, is_reg: typing.Optional[bool] = None, is_admin: typing.Optional[bool] = None):
        self.is_reg = is_reg
        self.is_admin = is_admin

    async def check(self, obj) -> bool:
        user_id = obj.from_user.id

        # Checking for a registered user
        if self.is_reg is False:
            user = SQLite(user_id=user_id)
            return (user.select_user is not None) == self.is_reg

        # Checking for an administrator
        if self.is_admin is True:
            return (user_id in admin_ids) == self.is_admin
