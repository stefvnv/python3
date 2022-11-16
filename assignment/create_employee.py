import contextlib
from tkinter import *
from io import BytesIO
from tkinter import messagebox

from PIL import Image, ImageTk
from tkcalendar import DateEntry

from Employee import *
from fonts import *
from database import *


def create_employee(window_portal):
    window_create = Toplevel(window_portal)
    window_create.geometry("720x1000")
    window_create.title("Employee Portal - Employee Management System | Add New Employee")
    window_create.resizable(False, False)
    window_create.config(bg="#B0B6A1")

    # ============ METHODS ============
    def add_to_database():
        new_id = entry_id.get()
        new_first_name = entry_first_name.get()

        new_employee = [(new_id, new_first_name)]

        cur.executemany("INSERT into Employee VALUES(?,?)", new_employee)
        con.commit()
        print("ADDED!!!!!!!!!!!!!!!!!!!")
        #cur.executemany("INSERT into Employee VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", new_employee)



    def on_closing():
        window_create.destroy()

    window_create.protocol("WM_DELETE_WINDOW", on_closing)

    # ============ GUI ============

    # ======Frame header======
    frame_header = Frame(window_create, width=720, height=60, bg="red")
    frame_header.place(x=0, y=0)

    # ======Title label======
    label_title = Label(frame_header, font=title_font, text="Employee Portal")
    label_title.place(x=10, y=0)

    # ======Current Employee ID label======
    label_current = Label(frame_header, font=subtitle_font)
    label_current.place(x=485, y=20)

    # ======Employee ID label======
    label_id = Label(window_create, text="Employee ID:")
    label_id.place(x=50, y=120)

    # ======Employee ID entry box======
    entry_id = Entry(window_create, width=30)
    entry_id.insert(END, '')
    entry_id.place(x=150, y=120)

    # ======First name label======
    label_first_name = Label(window_create, text="First Name:")
    label_first_name.place(x=50, y=200)

    # ======First name entry box======
    entry_first_name = Entry(window_create, width=30)
    entry_first_name.insert(END, '')
    entry_first_name.place(x=150, y=200)

    # ======Surname label======
    label_surname = Label(window_create, text="Surname:")
    label_surname.place(x=50, y=280)

    # ======Surname entry box======
    entry_surname = Entry(window_create, width=30)
    entry_surname.insert(END, '')
    entry_surname.place(x=150, y=280)

    # ======Gender label======
    label_gender = Label(window_create, text="Gender:")
    label_gender.place(x=50, y=360)

    # ======Gender radio buttons======
    rb_gender = IntVar()

    radiobutton_male = Radiobutton(window_create, text="Male", variable=rb_gender, value=1)
    radiobutton_male.place(x=150, y=360)

    radiobutton_female = Radiobutton(window_create, text="Female", variable=rb_gender, value=2)
    radiobutton_female.place(x=260, y=360)

    # ======Department label======
    label_surname = Label(window_create, text="Department:")
    label_surname.place(x=50, y=440)

    # ======Department option menu======
    list_departments = ["Business Development", "Services", "Marketing", "Engineering", "Training", "Legal",
                        "Human Resources", "Sales", "Product Management", "Support", "Product Management"]
    department = StringVar()
    option_menu_department = OptionMenu(window_create, department, *list_departments)
    option_menu_department.place(x=150, y=440)

    # ======Position label======
    label_position = Label(window_create, text="Position:")
    label_position.place(x=380, y=440)

    # ======Position entry box======
    entry_position = Entry(window_create, width=30)
    entry_position.insert(END, '')
    entry_position.place(x=480, y=440)

    # ======Date of birth label======
    label_dob = Label(window_create, text="Date of Birth:")
    label_dob.place(x=50, y=520)

    # ======Date of birth date entry======
    date_entry_dob = DateEntry(window_create, width=12, borderwidth=2)
    date_entry_dob.place(x=150, y=520)

    # ======Start date label======
    label_start_date = Label(window_create, text="Start Date:")
    label_start_date.place(x=380, y=520)

    # ======Start date date entry======
    date_entry_start_date = DateEntry(window_create, width=12, borderwidth=2)
    date_entry_start_date.place(x=480, y=520)

    # ======Email label======
    label_email = Label(window_create, text="Email:")
    label_email.place(x=50, y=600)

    # ======Email entry box======
    entry_email = Entry(window_create, width=30)
    entry_email.insert(END, '')
    entry_email.place(x=150, y=600)

    # ======Contact label======
    label_contact = Label(window_create, text="Contact:")
    label_contact.place(x=380, y=600)

    # ======Contact entry box======
    entry_contact = Entry(window_create, width=30)
    entry_contact.insert(END, '')
    entry_contact.place(x=480, y=600)

    # ======Salary label======
    label_salary = Label(window_create, text="Salary:")
    label_salary.place(x=50, y=640)

    # ======Salary entry box======
    spinbox_salary = Spinbox(window_create, from_=0, to=1000000, increment=1000)
    spinbox_salary.place(x=150, y=640)

    # ======Active label======
    label_active = Label(window_create, text="Active:")
    label_active.place(x=380, y=640)

    # ======Active radio buttons======
    rb_active = IntVar()

    radiobutton_yes = Radiobutton(window_create, text="Yes", variable=rb_active, value=1)
    radiobutton_yes.place(x=450, y=640)

    radiobutton_no = Radiobutton(window_create, text="No", variable=rb_active, value=2)
    radiobutton_no.place(x=500, y=640)

    # ======Address label======
    label_address = Label(window_create, text="Address:")
    label_address.place(x=50, y=720)

    # ======Address label======
    text_address = Text(window_create, width=64, height=10)
    text_address.place(x=150, y=720)

    # ======Picture label======
    label_picture = Label(window_create, relief="raised")
    label_picture.place(x=460, y=120)

    # ======Add button======
    button_add = Button(window_create, text="Add", command=add_to_database)
    button_add.place(x=340, y=900)
