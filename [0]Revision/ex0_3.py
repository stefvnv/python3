from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


def stepUp():
    value1 = int(entry2.get())
    value2 = int(entry3.get())
    value1 = value1 + value2
    entry2.delete(0, END)
    entry2.insert(END, value1)


def stepDown():
    value1 = int(entry2.get())
    value2 = int(entry4.get())
    value1 = value1 - value2
    entry2.delete(0, END)
    entry2.insert(END, value1)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

label1 = Label(window, text="Grid example", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)

label2 = Label(frame, text="Value", fg="blue", width=15, font=("arial", 10, "bold"))
label2.grid(row=0, column=0, sticky=W + E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W + E)

button1 = Button(frame, text="StepUp", fg="black", font=("arial", 10, "bold"), command=stepUp)
button1.grid(row=1, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '1')
entry3.grid(row=1, column=1, sticky=W + E)

button2 = Button(frame, text="StepDown", fg="black", font=("arial", 10, "bold"), command=stepDown)
button2.grid(row=2, column=0, sticky=W + E)

entry4 = Entry(frame)
entry4.insert(END, '1')
entry4.grid(row=2, column=1, sticky=W + E)

mainloop()
