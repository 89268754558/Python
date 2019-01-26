import sqlite3

#SQLite --- without server
#MySQL --- with server, admin\user permissions, etc.

conn = sqlite3.connect('connection.db') #connection
cur = conn.cursor() #make cursor

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS projectDataBase(unix REAL, data TEXT, key TEXT, val REAL)")


def data_entry():
    cur.execute("INSERT INTO projectDataBase VALUES(1345, 'Something', 'Lol', 25)")
    conn.commit()
    cur.close()
    conn.close()

create_table()
data_entry()


