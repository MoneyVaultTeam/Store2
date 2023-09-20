import sqlite3

conn = sqlite3.connect('file.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         ID     TEXT    NOT NULL,
         file          TEXT    NOT NULL,
         fid         TEXT    NOT NULL
        
         
         
);''')
print ("Table created successfully")
conn.close()