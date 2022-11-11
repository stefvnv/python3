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

    def to_string(self):
        return str(self.number + ", " + self.name)


#def display(index):


# name_entry.delete(0, END)
# name_entry.insert(END, employee.read_name())


# def update():
#
#
#
# def fillout():
#
#
#
# def check():



employee1 = Employee("555", "Mary Jane")
employee2 = Employee("3", "Peter Parker")

employee_list = [employee1, employee2]
employee_text_list = ""
for item in employee_list:
    employee_text_list += item.to_string() + "\n"

print(employee_text_list)


entry_search = Entry(window)
entry_search.insert(END, '')
entry_search.place(x=100, y=300)

# id_label = Label(window, text="ID", fg="blue", width=15, font=("arial", 10, "bold"))
# id_label.place(x=200, y=400)
#
# id_listbox = Listbox(window, font=("arial", 10, "bold"), width=100)
# id_listbox.place(x=200, y=500)
#
# name_label = Label(window, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))
# name_label.place(x=600, y=400)
#
# name_entry = Entry(window)
# name_entry.insert(END, '')
# name_entry.place(x=600, y=500)
#
# #display(0)
#
# update(employee_list)
#
# id_listbox.bind("<<ListboxSelect>>", fillout)
# entry_search.bind("KeyRelease", check)

mainloop()
