from tkinter import *

window = Tk()
window.geometry("1280x720")
window.title("Employee Portal | Employee Management System")
window.resizable(False, False)


# testing


class Employee:
    def __init__(self, emp_number, emp_name):
        self.number = emp_number
        self.name = emp_name

    def read_number(self):
        return self.number

    def read_name(self):
        return self.name


def display(index):
    global current
    global employee
    employee = employee_list[index]
    current = index

    listbox.delete(0, END)
    listbox.insert(END, employee.read_number())

    entry3.delete(0, END)
    entry3.insert(END, employee.read_name())


def update(data):
    listbox.delete(0, END)

    for item in data:
        listbox.insert(END, item)


def fillout(e):
    entry_search.delete(0, END)
    entry_search.insert(0, listbox.get(ANCHOR))


def check(e):
    typed = entry_search.get()

    if typed == '':
        data = employee_list
    else:
        data = []

        for item in employee_list:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)


employee1 = Employee("555", "Mary Jane")
employee2 = Employee("3", "Peter Parker")

employee_list = [employee1, employee2]

global current
global employee
employee = employee_list[0]

#
label1 = Label(window, text="Product Application", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)

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

update(employee_list)

listbox.bind("<<ListboxSelect>>", fillout)
entry_search.bind("KeyRelease", check)

mainloop()
