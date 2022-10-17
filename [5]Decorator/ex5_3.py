from tkinter import *

from ex5_3_class import *

window = Tk()
window.geometry("300x400")
window.title("Welcome")


# ============================================================
# Event Handling Methods

def display(index):
    global current
    global book
    book = booklist[index]
    current = index
    entry2.delete(0, END)
    entry2.insert(END, book.getTitle())
    entry3.delete(0, END)
    entry3.insert(END, book.getISBN())
    entry4b.delete(0, END)
    entry4b.insert(END, str(book.getPrice()))
    entry4.delete(0, END)
    entry4.insert(END, str(book.getWeight()))
    entry4c.delete(0, END)
    entry4c.insert(END, book.getBookType())

    # if (book.getPriority()==True):
    #    cb1.select()
    # else:
    #    cb1.deselect()
    entry5.delete(0, END)
    entry5.insert(END, '')
    entry5b.delete(0, END)
    entry5b.insert(END, '')
    entry6.delete(0, END)
    entry6.insert(END, '')


def addNewMethod():
    # student.markPresent()
    title = entry2.get()
    ISBN = entry3.get()
    weight = int(entry4.get())
    price = int(entry4b.get())

    newBook = factory.getBook(title, ISBN, weight, price)
    booklist.append(newBook)
    display(len(booklist) - 1)


def updatePriceMethod():
    price = int(entry5.get())
    book.updatePrice(price)
    display(current)


def updateWeightMethod():
    title = entry2.get()
    ISBN = entry3.get()
    weight = int(entry5b.get())
    price = int(entry4b.get())

    newBook = factory.getBook(title, ISBN, weight, price)
    booklist[current] = newBook
    display(current)


def calculateDeliveryPrice():
    plusDelivery = int(book.getDeliveryPrice())
    entry6.delete(0, END)
    entry6.insert(END, ("€" + str(plusDelivery)))


def nextCmd():
    global current
    if (current < (len(booklist) - 1)):
        current += 1
        display(current)


def prevCmd():
    global current
    if (current > 0):
        current -= 1
        display(current)


def firstCmd():
    display(0)


def lastCmd():
    display(len(booklist) - 1)


def clearMethod():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry4b.delete(0, END)
    entry4c.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


# End of Method Declarations
# ========================================================================


# Definitions
# =====================================================================
factory = BookFactory()
book1 = factory.getBook("Java Basics", "B23134", 202, 45)
book2 = factory.getBook("C# Unleashed", "C23123", 352, 55)
book3 = factory.getBook("Learn Python", "F2315", 421, 88)
book4 = factory.getBook("C Algorithms", "L66634", 570, 55)
book5 = factory.getBook("Intro to Java", "K77661", 216, 77)

booklist = [book1, book2, book3, book4, book5]
global current  # current student
global book
book = booklist[0]  # initialize to first student

# ========= End of Definitions ============================

# =======================================================
# Menu to Add New Student
menu1 = Menu(window)  # MenuBar
window.config(menu=menu1)
subm1 = Menu(menu1)  # Menu
menu1.add_cascade(label="Add_Book_Options", menu=subm1)
subm1.add_command(label="clearData", font=("arial", 12, "bold"), command=clearMethod)  # menu item
subm1.add_command(label="Insert Book", font=("arial", 12, "bold"), command=addNewMethod)

# ======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

label1 = Label(window, text="Book Factory", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)  # place on screen

label2 = Label(frame, text="Title", fg="blue", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="ISBN", fg="blue", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W + E)

label4 = Label(frame, text="Weight (g)", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4.grid(row=2, column=0, sticky=W + E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W + E)

label4b = Label(frame, text="Price €", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4b.grid(row=3, column=0, sticky=W + E)

entry4b = Entry(frame)
entry4b.insert(END, '0')
entry4b.grid(row=3, column=1, sticky=W + E)

label4c = Label(frame, text="Weight Category", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4c.grid(row=4, column=0, sticky=W + E)

entry4c = Entry(frame)
entry4c.insert(END, '0')
entry4c.grid(row=4, column=1, sticky=W + E)

# var_priority = IntVar()  # 0 unchecked, 1 checked
# cb1 = Checkbutton(frame, text="Priority", variable=var_priority)
# cb1.grid(row=4,column=0,columnspan=2)

button1 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clearMethod)
button1.grid(row=5, column=0, sticky=W + E)

button2 = Button(frame, text="addBook", fg="black", font=("arial", 10, "bold"), command=addNewMethod)
button2.grid(row=5, column=1, sticky=W + E)

button3 = Button(frame, text="updatePrice", fg="black", font=("arial", 10, "bold"), command=updatePriceMethod)
button3.grid(row=6, column=0, sticky=W + E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=6, column=1, sticky=W + E)

button3b = Button(frame, text="updateWeight", fg="black", font=("arial", 10, "bold"), command=updateWeightMethod)
button3b.grid(row=7, column=0, sticky=W + E)

entry5b = Entry(frame)
entry5b.insert(END, '0')
entry5b.grid(row=7, column=1, sticky=W + E)

button4 = Button(frame, text="calcDeliveryPrice", fg="red", font=("arial", 10, "bold"), command=calculateDeliveryPrice)
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
