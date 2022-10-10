from tkinter import *

window = Tk()
window.geometry("350x300")
window.title("Welcome")

from ex4_2_class import *


# ------------end of class definition------------------

def display():
    value1 = a1.getValue()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, a1.readMessage())


def incrementEvent():
    a1.increment()
    display()
    a1.writeMessage('')


def decrementEvent():
    a1.decrement()
    display()
    a1.writeMessage('')


    # a1 = Counter(10)
    # a1 = UpperLimit(Counter(10))
    # a1 = LowerLimit(Counter(10))


a1 = Warn(LowerLimit(UpperLimit(Counter(10))))

label1 = Label(window, text="Counter Details", fg="blue", bg="yellow", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

button4 = Button(window, text="Increment", fg="black", font=("arial", 10, "bold"), command=incrementEvent)
button4.place(x=40, y=120)

button5 = Button(window, text="Decrement", fg="black", font=("arial", 10, "bold"), command=decrementEvent)
button5.place(x=120, y=120)

label3 = Label(window, text="Message", fg="blue", width=8, font=("arial", 10, "bold"))  #
label3.place(x=10, y=160)

entry6 = Entry(window, width=40)
entry6.insert(END, '')
entry6.place(x=90, y=160)
display()

mainloop()
