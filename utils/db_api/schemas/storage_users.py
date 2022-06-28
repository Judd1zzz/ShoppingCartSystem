import sqlite3


# Creation table with storing user data
def create_storage_users(path_to_db) -> None:
    with sqlite3.connect(path_to_db) as db:
        check_sql = db.execute("PRAGMA table_info(storage_users)").fetchall()
        check_create_users = [c for c in check_sql]
        match len(check_create_users):
            case 3:
                print("storage_users was found      (1/4)")
            case _:
                db.execute("CREATE TABLE storage_users("
                        "increment INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "user_id INTEGER UNIQUE, "
                        "user_name TEXT)")
                print("Table storage_users was not found      (1/4) | Creating...")
        db.commit()