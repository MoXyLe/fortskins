import os
import sqlite3

name_db = 'db.sqlite3'
cur_dir = os.getcwd()
path_db = os.path.join(cur_dir, name_db)

conn = None
try:
    conn = sqlite3.connect(path_db)
except Error as e:
    print(e)

sql = 'DELETE FROM main_cosmetic'
cur = conn.cursor()
cur.execute(sql)
conn.commit()
