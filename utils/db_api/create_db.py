from .schemas import *
from data.config import load_config


# Create all tables for DB
def create_all() -> None:
    path = load_config(".env").db.path
    create_storage_users(path)
    create_storage_categories(path)
    create_storage_positions(path)
    create_storage_cart(path)
