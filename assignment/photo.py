import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from io import BytesIO
from PIL import Image, ImageTk

import sqlite3

con = sqlite3.connect("../employees.db")
cur = con.cursor()


try:
    cur.execute(
        "CREATE TABLE Employee(emp_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(45), surname VARCHAR(45), "
        "gender VARCHAR(10), department VARCHAR(100), position VARCHAR(45), date_of_birth VARCHAR(10), start_date "
        "VARCHAR(10), email VARCHAR(60), contact VARCHAR(20), salary INTEGER(12), active BLOB, address VARCHAR(100), "
        "picture BLOB)")
    data = [
        (543, "Peter", "Parker", "Male", "IT", "Senior Software Engineer", "12/03/85", "05/11/16",
         "peterparker@gmail.com", "732-234-1248", 120000, True, "5432 Apple St,\nMaineville,\nWA 43171",
         "./images/peter.jpg"),
        (201, "Mary Jane", "Watson", "Female", "Accounting", "Tax Accountant", "24/07/89", "17/05/20",
         "mary_accounting@yahoo.co.uk", "874-345-8654", 76000, True, "8541 Summer Ave,\nPullman,\nNY 27811",
         "./images/mary.jpg")]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

except:
    print("Employees database has not been created as it already exists.")

my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title('www.plus2net.com')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='Add Student Data with Photo', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(my_w, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=1)


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 = tk.Button(my_w, image=img)  # using Button
    b2.grid(row=3, column=1)


my_w.mainloop()  # Keep the window open
