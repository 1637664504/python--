import time
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

n = 5
while n > 0:
    cur.execute("select * from stocks")
    item = cur.fetchall()
    print('item: ',item)
    n=n-1
    time.sleep(2)


con.close()