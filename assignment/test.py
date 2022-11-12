import sqlite3
from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Employee Portal | Employee Management System")
window.resizable(False, False)

# testing

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
        (543, "Peter", "Parker", "Male", "IT", "Senior Software Engineer", "12/03/1985",
         "05/11/2016,peterparker@gmail.com", "0831239876", 120000, True, "5432 Apple St,\nMaineville,\nWA 43171",
         "peter.jpg"),
        (201, "Mary Jane", "Watson", "Female", "Accounting", "Tax Accountant", "24/07/1989", "17/05/2020",
         "peterparker@gmail.com", "0831239876", 120000, True, "8541 Summer Ave,\nPullman,\nNY 27811", "mary.jpg")]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

except:
    print("Employee Already Exists")




# MAKE THIS INTO ANOTHER CLASS
class Employee:
    def __init__(self, emp_id, emp_name):
        self.id = emp_id
        self.name = emp_name

    def read_id(self):
        return str(self.id)

    def read_name(self):
        return self.name

    def to_string(self):
        return str(self.id + ", " + self.name)


cur.execute("select * from Employee")
doubArray = cur.fetchall()

emp_list = []

for emp in doubArray:
    emp_list.append(Employee(emp[0], emp[1]))

emp_id_list = []
for emp_id in emp_list:
    emp_id_list.append(emp_id.read_id())

for x in emp_list:
    print(x.read_name())


def update(data_list):
    listbox_id.delete(0, END)

    for item in data_list:
        listbox_id.insert(END, item)


def fillout(e):
    current_index = 0

    entry_search.delete(0, END)
    entry_search.insert(0, listbox_id.get(ANCHOR))

    for iter_8 in range(len(emp_list)):
        if emp_list[iter_8].read_id() == listbox_id.get(ANCHOR):
            current_index = iter_8

    entry_name.delete(0, END)
    entry_name.insert(END, emp_list[current_index].read_name())

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


entry_search = Entry(window)
entry_search.insert(END, '')
entry_search.place(x=150, y=50)

listbox_id = Listbox(window)
listbox_id.place(x=200, y=200)

label_name = Label(window, text="Name")
label_name.place(x=150, y=400)

entry_name = Entry(window)
entry_name.insert(END, '')
entry_name.place(x=200, y=400)

update(emp_id_list)

listbox_id.bind("<<ListboxSelect>>", fillout)
entry_search.bind("<KeyRelease>", check)

mainloop()
