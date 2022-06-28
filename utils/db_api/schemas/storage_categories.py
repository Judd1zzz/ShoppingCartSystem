import sqlite3


# Creating a table with category data storage
def create_storage_categories(path_to_db) -> None:
    with sqlite3.connect(path_to_db) as db:
        check_sql = db.execute("PRAGMA table_info(storage_categories)").fetchall()
        check_create_products = [c for c in check_sql]
        match len(check_create_products):
            case 2:
                print("storage_categories was found (2/4)")
            case _:
                db.execute("CREATE TABLE storage_categories("
                        "id INTEGER UNIQUE, "
                        "name TEXT)")
                print("Table storage_categories was not found (2/4) | Creating...")
        db.commit()