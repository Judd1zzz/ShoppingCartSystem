import sqlite3


# Creating a table with position data storage
def create_storage_positions(path_to_db) -> None:
    with sqlite3.connect(path_to_db) as db:
        check_sql = db.execute("PRAGMA table_info(storage_positions)").fetchall()
        check_create_products = [c for c in check_sql]
        match len(check_create_products):
            case 4:
                print("storage_positions was found  (3/4)")
            case _:
                db.execute("CREATE TABLE storage_positions("
                        "name TEXT, "
                        "price INTEGER, "
                        "id INTEGER UNIQUE, "
                        "category_id INTEGER)")
                print("Table storage_positions was not found  (3/4) | Creating...")
        db.commit()