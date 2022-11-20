import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

con = sqlite3.connect("../test.db")
cur = con.cursor()

try:
    # my_conn.execute('DROP TABLE student')
    con.execute('''
        CREATE TABLE IF NOT EXISTS student(id integer primary key, 
                      name text, 
                      class text, 
                      mark integer, 
                      gender text,
                      photo blob 
                      );''')
except SQLAlchemyError as e:
    # print(e)
    error = str(e.__dict__['orig'])
    print(error)
else:
    print("Test Table created successfully..")
