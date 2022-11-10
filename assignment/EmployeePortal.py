import sqlite3
from tkinter import *
from Employee import *

window = Tk()
window.geometry("1280x720")
window.title("Employee Portal | Employee Management System")
window.resizable(False, False)


# Methods to display data
def display(index):
    global current
    global employee

    cur.execute("select * from Employee")

    current_emp = cur.fetchall()[index]

    current = index

    # DELETE ALL ENTRIES AND INSERT CURRENT EMPLOYEE[0]


# Database
con = sqlite3.connect("../tutorial.db")
cur = con.cursor()

try:
    # cur.execute("DROP TABLE Movie")
    cur.execute("CREATE TABLE Employee(emp_number, first_name, last_name, gender, department)")
    data = [
        ("5432", "Peter", "Parker", "Male", "IT"),
        ("345", "Mary", "Jane", "Female", "Accounting"),
        ("22", "Adam", "Sandler", "Male", "Marketing"), ]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?)", data)
    con.commit()

except:
    print("Employee Already Exists")

#
label_title = Label(window, text="Product Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label_title.place(x=90, y=30)

entry_search = Entry(window)
entry_search.insert(END, '')
entry_search.place(x=100, y=300)

label2 = Label(window, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))
label2.place(x=200, y=400)

listbox = Listbox(window, font=("arial", 10, "bold"))
listbox.place(x=200, y=500)

label3 = Label(window, text="Price", fg="blue", width=15, font=("arial", 10, "bold"))
label3.place(x=600, y=400)

entry3 = Entry(window)
entry3.insert(END, '')
entry3.place(x=600, y=500)

display(0)

mainloop()


#to do
#connect to employee gui based on employee