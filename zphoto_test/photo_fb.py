import sqlite3
import tkinter as tk
from tkinter import *
from PIL import ImageTk

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

my_w = tk.Tk()
my_w.geometry("700x550")  # Size of the window
my_w.title("www.plus2net.com")  # title


# connection to SQLite database
con = sqlite3.connect("../test.db")
cur = con.cursor()

l1 = tk.Label(my_w, text='Display Image from SQLite Database', width=30, font=20)
l1.grid(row=0, column=1, padx=10, pady=10)
b1 = tk.Button(my_w, text='Show Data',
               width=20, command=lambda: show_data())
b1.grid(row=1, column=1)
img = []


def show_data():
    global img  # Image variable to display
    my_data = (54)  # ID of the row to display
    q = "SELECT * FROM  student WHERE id=?"  # query with place holders
    try:
        my_cursor = con.execute(q, my_data)
        r_set = my_cursor.fetchone()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    else:
        student = str(r_set[0]) + ',' + r_set[1] + ',' + r_set[2] + ',' + str(r_set[3])
        l2.config(text=student)  # show student data other than image

        img = ImageTk.PhotoImage(data=r_set[5])  # create image
        l3.config(image=img)  # display image


l2 = tk.Label(my_w, text='Data here ', font=20)
l2.grid(row=2, column=1)
l3 = tk.Label(my_w, text='Image here ')
l3.grid(row=3, column=1)
my_w.mainloop()  # Keep the window open
