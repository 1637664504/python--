import time
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

# cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test';")
# print(cur.fetchall()) --> 空

cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stocks';")
ret = cur.fetchall()
if not ret:
    # Create table
    cur.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')

n = 5
while n > 0:
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
    cur.execute("""INSERT INTO stocks VALUES (?,'BUY','RHAT',100,35.14);""",(now_time,))
    con.commit()
    n=n-1
    time.sleep(2)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

''' 
结论:
只有执行con.commit()动作

'''