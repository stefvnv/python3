import sqlite3
import tkinter as tk
from tkinter import filedialog

my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title("www.plus2net.com")  # title

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

con = sqlite3.connect("../test.db")
cur = con.cursor()

l1 = tk.Label(my_w, text='Upload File & add Binary data ', width=30, font=20)
l1.grid(row=0, column=1, padx=10, pady=10)
b1 = tk.Button(my_w, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=1, column=1)


def upload_file():
    file = filedialog.askopenfilename()
    fob = open(file, 'rb')
    blob_data = fob.read()  # Binary data is ready
    my_data = [(None, 'Tes Qry', 'Six', 78, 'male', blob_data)]  # Data to store
    q = "INSERT INTO student values(?,?,?,?,?,?)"  # query with place holders
    try:
        r_set = con.execute(q, my_data)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        l1.config(text="Data Added , ID: " + str(r_set.lastrowid))


my_w.mainloop()  # Keep the window open
