import sqlite3
from tkinter import *
from time import strftime
from tkinter import Tk, messagebox
from instance import *
from Employee import *
import tkinter as tk

# variables
global counter
counter = 1

# Database
con = sqlite3.connect("../employees.db")
cur = con.cursor()

try:
    cur.execute(
        "CREATE TABLE Employee(emp_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(45), surname VARCHAR(45), "
        "gender VARCHAR(10), department VARCHAR(100), position VARCHAR(45), date_of_birth VARCHAR(10), start_date "
        "VARCHAR(10), email VARCHAR(60), contact VARCHAR(15), salary INTEGER(12), active BLOB, address VARCHAR(100), "
        "picture BLOB)")
    data = [
        (543, "Peter", "Parker", "Male", "IT", "Senior Software Engineer", "12/03/1985", "05/11/2016",
         "peterparker@gmail.com", "0831239876", 120000, True, "5432 Apple St,\nMaineville,\nWA 43171", "peter.jpg"),
        (201, "Mary Jane", "Watson", "Female", "Accounting", "Tax Accountant", "24/07/1989", "17/05/2020",
         "mary_accounting@yahoo.co.uk", "0879595321", 76000, True, "8541 Summer Ave,\nPullman,\nNY 27811", "mary.jpg")]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

except:
    print("Employee database has not been created as it already exists.")


# ADD ALL GUI STUFF INSIDE THIS METHOD
def initiate_portal(window):
    """Initiates the GUI"""

    window_portal = Toplevel(window)
    window_portal.geometry("1280x720")
    window_portal.title("Employee Portal - Employee Management System")
    window_portal.resizable(False, False)

    def live_clock():
        time_string = strftime("%A, %d %B, %H:%M:%S %p")
        label_clock.config(text=time_string)
        label_clock.after(1000, live_clock)

    def search():
        cur.execute("SELECT * FROM Employee")

        array_2d = cur.fetchall()

        emp_list = []

        for emp in array_2d:
            emp_list.append(
                Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10],
                         emp[11], emp[12], emp[13]))

        emp_id_list = []
        for emp_id in emp_list:
            emp_id_list.append(emp_id.read_id())

        def update(data_list):
            listbox_id.delete(0, END)

            for item in data_list:
                listbox_id.insert(END, item)

        def fill(e):
            current_index = 0

            entry_search.delete(0, END)
            entry_search.insert(0, listbox_id.get(ANCHOR))

            for iter_8 in range(len(emp_list)):
                if emp_list[iter_8].read_id() == listbox_id.get(ANCHOR):
                    current_index = iter_8

            entry_first_name.delete(0, END)
            entry_first_name.insert(END, emp_list[current_index].read_first_name())

            entry_surname.delete(0, END)
            entry_surname.insert(END, emp_list[current_index].read_surname())

            entry_position.delete(0, END)
            entry_position.insert(END, emp_list[current_index].read_position())

            # complete for each of the entry boxes

        def check(e):
            typed = entry_search.get()
            if typed == '':
                info = []
                for x in emp_list:
                    info.append(x.read_id())
            else:
                info = []

                for item in emp_id_list:
                    if typed in item:
                        info.append(item)
            update(info)

        update(emp_id_list)

        listbox_id.bind("<<ListboxSelect>>", fill)
        entry_search.bind("<KeyRelease>", check)

    # FIX - CHECK IF INSTANCE IS ALREADY OPEN
    def view_employee():
        global counter

        # ensures employee tab can only be opened once
        if counter < 2:
            display_employee(window_portal)
            counter += 1
        else:
            messagebox.showinfo("Information", "Only one employee can be viewed at a time.")

    # GUI

    # ======Frame Header======
    frame_header = Frame(window_portal, width=1280, height=60, bg="red")
    frame_header.place(x=0, y=0)

    # ======Live clock======
    label_clock = tk.Label(frame_header)
    label_clock.place(x=10, y=10)

    # ======Title label======
    label_title = Label(frame_header, text="Employee Portal Dashboard")
    label_title.place(x=400, y=10)

    # ======Search label======
    label_search = Label(frame_header, text="Search (by ID):")
    label_search.place(x=900, y=30)

    # ======Search entry box======
    entry_search = Entry(frame_header, width=40)
    entry_search.insert(END, '')
    entry_search.focus_set()
    entry_search.place(x=1000, y=30)

    # ======Employee ID label======
    label_id = Label(window_portal, text="Employee ID:")
    label_id.place(x=100, y=120)

    # ======Employee ID listbox======
    listbox_id = Listbox(window_portal, width=40, height=5)
    listbox_id.place(x=300, y=120)

    # ======First name label======
    label_first_name = Label(window_portal, text="First Name:")
    label_first_name.place(x=100, y=200)

    # ======First name entry box======
    entry_first_name = Entry(window_portal, width=40)
    entry_first_name.insert(END, '')
    entry_first_name.place(x=300, y=200)

    # ======Surname label======
    label_surname = Label(window_portal, text="Surname:")
    label_surname.place(x=100, y=280)

    # ======Surname entry box======
    entry_surname = Entry(window_portal, width=40)
    entry_surname.insert(END, '')
    entry_surname.place(x=300, y=280)

    # ======Position label======
    label_position = Label(window_portal, text="Position:")
    label_position.place(x=100, y=360)

    # ======Position entry box======
    entry_position = Entry(window_portal, width=40)
    entry_position.insert(END, '')
    entry_position.place(x=300, y=360)

    # ======View employee button======
    button_view_employee = Button(window_portal, text="View/Edit Full Employee Profile", command=view_employee)
    button_view_employee.place(x=200, y=400)

    # start methods
    search()
    live_clock()
