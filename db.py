import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS users (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT NOT NULL UNIQUE
# );
# """
# )
cursor.execute("DELETE FROM users WHERE id=1")
print("Запись с id=3 успешно удалена")
conn.commit()
# print("Таблица 'users' успешно создана (или уже существовала).")
# db.close()
