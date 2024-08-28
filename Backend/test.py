from core.container.monit import monit_conatiner
from core.system.monit import monit_system
from core.database.db import Database



# import sqlite3

# conn = sqlite3.connect('./store.db')
# cur = conn.cursor()

# try:
#     cur.execute('''CREATE TABLE users
#                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

#     conn.commit()
# except:
#     print("already exists")

# cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("test", 10))

# conn.commit()

# cur.execute("SELECT * FROM users")

# response = cur.fetchall()
# print(response)

# conn.close()

database = Database()

response = database.select("system")
print(response)
monit_system(database)
