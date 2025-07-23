import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("UPDATE users set name='Dog' where id=1")
conn.commit()
conn.close()