import sqlite3
import time
import datetime
import random

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

def dynamic_add():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    #cur.execute("INSERT INTO projectDataBase (unix, data, key, val)  VALUES(?,?,?,?)",(unix, date, keyword, value))
    cur.execute("INSERT INTO projectDataBase  VALUES(%i,'%s','%s',%i)"%(unix, date, keyword, value))
    conn.commit()



def read_from():
    #cur.execute("SELECT * FROM projectDataBase")
    #cur.execute("SELECT * FROM projectDataBase WHERE val = 3")
    #cur.execute("SELECT * FROM projectDataBase WHERE val = 3 AND ....")
    cur.execute("SELECT unix, key, val, data FROM projectDataBase WHERE val > 3 AND unix > 10000")
    ##data = cur.fetchall()
    ##print(data)
    for row in cur.fetchall():
        print(row)


def delete_update():
    cur.execute("SELECT * FROM projectDataBase")
    [print(row) for row in cur.fetchall()]
    cur.execute("UPDATE projectDataBase SET val = 999 WHERE val < 4")
    conn.commit()
    

    cur.execute("SELECT * FROM projectDataBase")
    [print(row) for row in cur.fetchall()]

#create_table()
#data_entry()
#for i in range(10):
#    dynamic_add()
#    time.sleep(1)

#read_from()
delete_update()
cur.close()
conn.close()