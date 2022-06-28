# - *- coding: utf- 8 - *-
import random
import sqlite3
from data.config import load_config
from .config_classes import PositionInfo, CategoryInfo


class SQLite:
    """Calling quick methods for convenience"""
    def __init__(self, user_id: int = 0, user_name: str = None, category_id: int = 0, position_id: int = 0) -> None:
        self.path_to_db = load_config(".env").db.path
        self.user_id = user_id
        self.user_name = user_name
        self.category_id = category_id
        self.position_id = position_id
    
    # Add user
    @property
    def add_user(self) -> None:
        with sqlite3.connect(self.path_to_db) as db:
            db.execute(f"INSERT INTO storage_users "
                       f"(user_id, user_name) "
                       f"VALUES (?, ?)", [self.user_id, self.user_name])
            db.commit()

    # Select user
    @property
    def select_user(self) -> tuple | None:
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"SELECT * FROM storage_users WHERE user_id = {self.user_id}").fetchone()

    # Check categories
    @property
    def check_categories(self) -> tuple | None:
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"SELECT * FROM storage_categories").fetchone()

    # Select category
    @property
    def select_category(self) -> CategoryInfo:
        with sqlite3.connect(self.path_to_db) as db:
            get_response = db.execute(f"SELECT * FROM storage_categories WHERE id = {self.category_id}").fetchone()
            category_id = get_response[0]
            category_name = get_response[1]
            return CategoryInfo(
                id=category_id,
                name=category_name
                )

    # Select all categories
    @property
    def select_all_categories(self):
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"SELECT * FROM storage_categories").fetchall()

    # Select all positions
    @property
    def select_all_positions(self) -> list[tuple | None]:
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"SELECT * FROM storage_positions WHERE category_id = {self.category_id}").fetchall()

    # Select position
    @property
    def select_position(self) -> PositionInfo | None:
        with sqlite3.connect(self.path_to_db) as db:
            get_response = db.execute(f"SELECT * FROM storage_positions WHERE id = {self.position_id}").fetchone()
            name = get_response[0]
            price = get_response[1]
            position_id = get_response[2]
            category_id = get_response[3]
            return PositionInfo(
                name=name,
                price=price,
                position_id=position_id,
                category_id=category_id
            )

    # Add position to cart
    @property
    def add_to_cart(self) -> None:
        with sqlite3.connect(self.path_to_db) as db:
            db.execute(f"INSERT INTO storage_cart "
                       f"(user_id, position_id) "
                       f"VALUES (?, ?)", [self.user_id, self.position_id])
            db.commit()

    # Check user cart
    @property
    def check_user_cart(self) -> tuple | None:
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"SELECT * FROM storage_cart WHERE user_id = {self.user_id}").fetchone()

    # Select user cart
    @property
    def select_user_cart(self) -> None:
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"SELECT * FROM storage_cart WHERE user_id = {self.user_id}").fetchall()

    # Delete user cart
    @property
    def delete_user_cart(self) -> None:
        with sqlite3.connect(self.path_to_db) as db:
            return db.execute(f"DELETE FROM storage_cart WHERE user_id = {self.user_id}")

    # Key generator (not useful)
    @staticmethod
    def _key_gen(shuffles_count: int = None) -> int:
        key = list(f'{str(random.randint(100000, 999999))}')
        match shuffles_count:
            case None:
                random.shuffle(key)
            case _:
                for _ in range(shuffles_count):
                    random.shuffle(key)
        key = int(''.join(key))
        return key
