# TEST FILE - to be deleted

from tkinter import *
from time import strftime
from tkinter import Tk, messagebox
from instance import *
import tkinter as tk


window_portal = Tk()
window_portal.geometry("1280x720")
window_portal.title("Welcome")
window_portal.resizable(False, False)


global counter
counter = 1


def live_clock():
    time_string = strftime("%A, %d %B, %H:%M:%S %p")
    label_clock.config(text=time_string)
    label_clock.after(1000, live_clock)


# FIX - CHECK IF INSTANCE IS ALREADY OPEN

def view_employee():
    global counter

    # ensures employee tab can only be opened once
    if counter < 2:
        display_employee(window_portal)
        counter += 1
    else:
        messagebox.showinfo("Information", "Only one employee can be viewed at a time.")


# GUI

# ======Frame Header======
frame_header = Frame(window_portal, width=1280, height=60, bg="red")
frame_header.place(x=0, y=0)

# ======Live clock======
label_clock = tk.Label(frame_header)
label_clock.place(x=10, y=10)

# ======Title label======
label_title = Label(frame_header, text="Employee Portal Dashboard")
label_title.place(x=400, y=10)

# ======Search label======
label_search = Label(frame_header, text="Search (by ID):")
label_search.place(x=900, y=30)

# ======Search entry box======
entry_search = Entry(frame_header, width=40)
entry_search.insert(END, '')
entry_search.focus_set()
entry_search.place(x=1000, y=30)


# ======Employee ID label======
label_id = Label(window_portal, text="Employee ID:")
label_id.place(x=100, y=120)

# ======Employee ID entry box======
entry_id = Entry(window_portal, width=40)
entry_id.insert(END, '')
entry_id.place(x=300, y=120)

# ======First name label======
label_first_name = Label(window_portal, text="First Name:")
label_first_name.place(x=100, y=200)

# ======First name entry box======
entry_first_name = Entry(window_portal, width=40)
entry_first_name.insert(END, '')
entry_first_name.place(x=300, y=200)

# ======Surname label======
label_surname = Label(window_portal, text="Surname:")
label_surname.place(x=100, y=280)

# ======Surname entry box======
entry_surname = Entry(window_portal, width=40)
entry_surname.insert(END, '')
entry_surname.place(x=300, y=280)

# ======Position label======
label_position = Label(window_portal, text="Position:")
label_position.place(x=100, y=360)

# ======Position entry box======
entry_position = Entry(window_portal, width=40)
entry_position.insert(END, '')
entry_position.place(x=300, y=360)

# ======View employee button======
button_view_employee = Button(window_portal, text="View or Change Full Employee Profile", command=view_employee)
button_view_employee.place(x=200, y=400)



# start methods
live_clock()
mainloop()
