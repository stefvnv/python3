from tkinter import *

from ex5_2_class import *

window = Tk()
window.geometry("300x400")
window.title("Welcome")


# ============================================================
# Event Handling Methods

def display(index):
    global current
    global customer
    customer = customerlist[index]
    current = index
    entry2.delete(0, END)
    entry2.insert(END, customer.getName())
    entry3.delete(0, END)
    entry3.insert(END, customer.getAge())
    entry4.delete(0, END)
    entry4.insert(END, customer.getGrossPrice())
    entry4b.delete(0, END)
    entry4b.insert(END, customer.getCustomerType())
    if (customer.getPriority() == True):
        cb1.select()
    else:
        cb1.deselect()
    entry5.delete(0, END)
    entry5.insert(END, '')
    entry5b.delete(0, END)
    entry5b.insert(END, '')
    entry6.delete(0, END)
    entry6.insert(END, '')


def addNewMethod():
    # student.markPresent()
    name = entry2.get()
    age = int(entry3.get())
    price = int(entry4.get())
    priority = False
    if var_priority.get() > 0:
        priority = True
    newCustomer = factory.getCustomer(name, age, priority, price)
    customerlist.append(newCustomer)
    display(len(customerlist) - 1)


def updatePriceMethod():
    price = int(entry5.get())
    customer.updatePrice(price)
    display(current)


def updateAgeMethod():
    name = entry2.get()
    age = int(entry5b.get())
    price = int(entry4.get())
    priority = False
    if (var_priority.get() > 0):
        priority = True
    newCustomer = factory.getCustomer(name, age, priority, price)
    customerlist[current] = newCustomer
    display(current)


def calculateNetMethod():
    adjusted = int(customer.getNetPrice())
    entry6.delete(0, END)
    entry6.insert(END, ("€" + str(adjusted)))


def percentAttended():
    None
    # result = student.getPercentAttendance()
    # entry7.delete(0, END)
    # entry7.insert(END, (str(result) + " %"))


def nextCmd():
    global current
    if current < (len(customerlist) - 1):
        current += 1
        display(current)


def prevCmd():
    global current
    if current > 0:
        current -= 1
        display(current)


def firstCmd():
    display(0)


def lastCmd():
    display(len(customerlist) - 1)


def clearMethod():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry4b.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


# End of Method Declarations
# ========================================================================


# Definitions
# =====================================================================
factory = CustomerFactory()
customer1 = factory.getCustomer("J.Smith", 22, True, 45)
customer2 = factory.getCustomer("L.Shine", 12, False, 55)
customer3 = factory.getCustomer("M.Jones", 21, True, 88)
customer4 = factory.getCustomer("T.Lennon", 57, False, 55)
customer5 = factory.getCustomer("H.Green", 16, True, 77)

customerlist = [customer1, customer2, customer3, customer4, customer5]
global current  # current student
global customer
customer = customerlist[0]  # initialize to first student

# ========= End of Definitions ============================

# =======================================================
# Menu to Add New Student
menu1 = Menu(window)  # MenuBar
window.config(menu=menu1)
subm1 = Menu(menu1)  # Menu
menu1.add_cascade(label="Add_Customer_Options", menu=subm1)
subm1.add_command(label="clearData", font=("arial", 12, "bold"), command=clearMethod)  # menu item
subm1.add_command(label="Insert Customer", font=("arial", 12, "bold"), command=addNewMethod)

# ======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

label1 = Label(window, text="Customer Factory", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)  # place on screen

label2 = Label(frame, text="Name", fg="blue", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="Age", fg="blue", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W + E)

label4 = Label(frame, text="Price", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4.grid(row=2, column=0, sticky=W + E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W + E)

label4b = Label(frame, text="Type", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4b.grid(row=3, column=0, sticky=W + E)

entry4b = Entry(frame)
entry4b.insert(END, '0')
entry4b.grid(row=3, column=1, sticky=W + E)

var_priority = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Priority", variable=var_priority)
cb1.grid(row=4, column=0, columnspan=2)

button1 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clearMethod)
button1.grid(row=5, column=0, sticky=W + E)

button2 = Button(frame, text="addNew", fg="black", font=("arial", 10, "bold"), command=addNewMethod)
button2.grid(row=5, column=1, sticky=W + E)

button3 = Button(frame, text="updatePrice", fg="black", font=("arial", 10, "bold"), command=updatePriceMethod)
button3.grid(row=6, column=0, sticky=W + E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=6, column=1, sticky=W + E)

button3b = Button(frame, text="updateAge", fg="black", font=("arial", 10, "bold"), command=updateAgeMethod)
button3b.grid(row=7, column=0, sticky=W + E)

entry5b = Entry(frame)
entry5b.insert(END, '0')
entry5b.grid(row=7, column=1, sticky=W + E)

button4 = Button(frame, text="calculateNetPrice", fg="red", font=("arial", 10, "bold"), command=calculateNetMethod)
button4.grid(row=8, column=0, sticky=W + E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=8, column=1, sticky=W + E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=9, column=0, sticky=W + E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=9, column=1, sticky=W + E)

button7 = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
button7.grid(row=10, column=0, sticky=W + E)

button8 = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
button8.grid(row=10, column=1, sticky=W + E)

display(0)

mainloop()
