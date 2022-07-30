import os
import sqlite3

PATH = os.path.abspath(os.path.dirname(__file__))
print(PATH)

connection = sqlite3.connect(f'{PATH}/database.db')

with open(f'{PATH}/shema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
