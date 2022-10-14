from tkinter import *

from ex5_1_class import *

window = Tk()
window.geometry("300x400")
window.title("Welcome")


# ============================================================
# Event Handling Methods

def display(index):
    global current
    global student
    student = studentlist[index]
    current = index
    entry2.delete(0, END)
    entry2.insert(END, student.getName())
    entry3.delete(0, END)
    entry3.insert(END, student.getAge())
    entry4.delete(0, END)
    entry4.insert(END, student.getMark())
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
    mark = int(entry4.get())
    newStudent = factory.getStudent(name, age, mark)
    studentlist.append(newStudent)
    display(len(studentlist) - 1)


def updateMarkMethod():
    mark = int(entry5.get())
    student.updateMark(mark)
    display(current)


def updateAgeMethod():
    name = entry2.get()
    age = int(entry5b.get())
    mark = int(entry4.get())
    newStudent = factory.getStudent(name, age, mark)
    studentlist[current] = newStudent
    display(current)


def adjustedMarkMethod():
    adjusted = student.getAdjustedMark()
    entry6.delete(0, END)
    entry6.insert(END, (str(adjusted) + " %"))


def percentAttended():
    None
    # result = student.getPercentAttendance()
    # entry7.delete(0, END)
    # entry7.insert(END, (str(result) + " %"))


def nextCmd():
    global current
    if current < (len(studentlist) - 1):
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
    display(len(studentlist) - 1)


def clearMethod():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)


# End of Method Declarations
# ========================================================================


# Definitions
# =====================================================================
factory = StudentFactory()
student1 = factory.getStudent("J.Smith", 22, 45)
student2 = factory.getStudent("L.Shine", 68, 55)
student3 = factory.getStudent("M.Jones", 21, 88)
student4 = factory.getStudent("T.Lennon", 57, 55)
student5 = factory.getStudent("H.Green", 20, 77)

studentlist = [student1, student2, student3, student4, student5]
global current  # current student
global student
student = studentlist[0]  # initialize to first student

# ========= End of Definitions ============================

# =======================================================
# Menu to Add New Student
menu1 = Menu(window)  # MenuBar
window.config(menu=menu1)
subm1 = Menu(menu1)  # Menu
menu1.add_cascade(label="Add_Student_Options", menu=subm1)
subm1.add_command(label="clearData", font=("arial", 12, "bold"), command=clearMethod)  # menu item
subm1.add_command(label="Insert Student", font=("arial", 12, "bold"), command=addNewMethod)

# ======= End of Menu Definition ============================

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

label1 = Label(window, text="Student Factory", fg="blue", bg="yellow", font=("arial", 16, "bold"))
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

label4 = Label(frame, text="Mark", fg="blue", width=15, font=("arial", 10, "bold"))  #
label4.grid(row=2, column=0, sticky=W + E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W + E)

button1 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clearMethod)
button1.grid(row=3, column=0, sticky=W + E)

button2 = Button(frame, text="addNew", fg="black", font=("arial", 10, "bold"), command=addNewMethod)
button2.grid(row=3, column=1, sticky=W + E)

button3 = Button(frame, text="updateMark", fg="black", font=("arial", 10, "bold"), command=updateMarkMethod)
button3.grid(row=4, column=0, sticky=W + E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=4, column=1, sticky=W + E)

button3b = Button(frame, text="updateAge", fg="black", font=("arial", 10, "bold"), command=updateAgeMethod)
button3b.grid(row=5, column=0, sticky=W + E)

entry5b = Entry(frame)
entry5b.insert(END, '0')
entry5b.grid(row=5, column=1, sticky=W + E)

button4 = Button(frame, text="adjustedMark", fg="red", font=("arial", 10, "bold"), command=adjustedMarkMethod)
button4.grid(row=6, column=0, sticky=W + E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=6, column=1, sticky=W + E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=7, column=0, sticky=W + E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=7, column=1, sticky=W + E)

button7 = Button(frame, text="First", fg="black", font=("arial", 10, "bold"), command=firstCmd)
button7.grid(row=8, column=0, sticky=W + E)

button8 = Button(frame, text="Last", fg="black", font=("arial", 10, "bold"), command=lastCmd)
button8.grid(row=8, column=1, sticky=W + E)

display(0)

mainloop()
