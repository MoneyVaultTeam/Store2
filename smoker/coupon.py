import sqlite3 

conn = sqlite3.connect('coupon.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID     TEXT    NOT NULL,
         code        TEXT    NOT NULL,
         date          TEXT    NOT NULL,
         amount           TEXT    NOT NULL
);''')
print ("Table created successfully")

conn.close()