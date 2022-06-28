import sqlite3


# Creating a table with cart data storage
def create_storage_cart(path_to_db) -> None:
    with sqlite3.connect(path_to_db) as db:
        check_sql = db.execute("PRAGMA table_info(storage_cart)").fetchall()
        check_create_cart = [c for c in check_sql]
        match len(check_create_cart):
            case 2:
                print("storage_cart was found       (4/4)")
            case _:
                db.execute("CREATE TABLE storage_cart("
                        "user_id INTEGER, "
                        "position_id INTEGER)")
                print("Table storage_cart was not found       (4/4) | Creating...")
        db.commit()