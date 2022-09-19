from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Adder:

    def __init__(self, name):
        self.__value = 0
        self.__name = name

    def add(self, amount):
        self.__value += amount

    def resetName(self, name):
        self.__name = name

    def resetValue(self, val):
        self.__value = val

    def getValue(self):
        return self.__value

    def getName(self):
        return self.__name


def display():
    value1 = a1.getValue()
    value2 = a1.getName()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry21.delete(0, END)  # delete old value
    entry21.insert(END, value2)


def resetNameEv():
    nm = entry42.get()
    a1.resetName(nm)
    display()


def resetValueEv():
    amt = int(entry41.get())
    a1.resetValue(amt)
    display()


def addEv():
    amt = int(entry5.get())
    a1.add(amt)
    display()


a1 = Adder('Population')

label1 = Label(window, text="Counter Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label3 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))  #
label3.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

entry21 = Entry(window)
entry21.insert(END, '1')
entry21.place(x=120, y=110)

label21 = Label(window, text="Name", fg="blue", width=8, font=("arial", 10, "bold"))  #
label21.place(x=10, y=110)

button4 = Button(window, text="ResetValue", fg="black", font=("arial", 9, "bold"), command=resetValueEv)
button4.place(x=40, y=140)

entry41 = Entry(window)
entry41.insert(END, '1')
entry41.place(x=120, y=140)

button42 = Button(window, text="resetName", fg="black", font=("arial", 9, "bold"), command=resetNameEv)
button42.place(x=40, y=170)

entry42 = Entry(window)
entry42.insert(END, '')
entry42.place(x=120, y=170)

button5 = Button(window, text="add", fg="black", font=("arial", 9, "bold"), command=addEv)
button5.place(x=40, y=200)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=200)

display()

mainloop()
