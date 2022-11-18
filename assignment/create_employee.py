import contextlib
from tkinter import *
from io import BytesIO
from tkinter import messagebox

from PIL import Image, ImageTk
from tkcalendar import DateEntry

from Employee import *
from fonts import *
from database import *


class EmployeeCreator:
    def __init__(self):
        self.__window_create = 0

    @staticmethod
    def read_window(self):
        return self.window_create

    @staticmethod
    def create_employee(self, window_portal):
        self.window_create = Toplevel(window_portal)
        self.window_create.geometry("720x1000")
        self.window_create.title("Employee Portal - Employee Management System | Add New Employee")
        self.window_create.resizable(False, False)
        self.window_create.config(bg="#B0B6A1")

        # ============ METHODS ============
        def add_to_database():
            new_id = entry_id.get()
            new_first_name = entry_first_name.get()
            new_surname = entry_surname.get()
            new_gender = rb_gender.get()
            new_department = department.get()
            new_position = entry_position.get()
            new_dob = date_entry_dob.get()
            new_email = entry_email.get()
            new_contact = entry_contact.get()
            new_salary = spinbox_salary.get()
            new_active = rb_active.get()
            new_address = text_address.get("1.0", END)

            # complete
            new_picture = ""

            new_employee = [
                (new_id, new_first_name, new_surname, new_gender, new_department, new_position, new_dob, new_email,
                 new_contact, new_salary, new_active, new_address, new_picture)]

            cur.executemany("INSERT into Employee VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", new_employee)
            con.commit()

            messagebox.showinfo("Employee Added", "Employee added to database successfully.")

        def on_closing():
            self.window_create.destroy()

        self.window_create.protocol("WM_DELETE_WINDOW", on_closing)

        # ============ GUI ============

        # ======Frame header======
        frame_header = Frame(self.window_create, width=720, height=60, bg="red")
        frame_header.place(x=0, y=0)

        # ======Title label======
        label_title = Label(frame_header, font=title_font, text="Employee Portal")
        label_title.place(x=10, y=0)

        # ======Current Employee ID label======
        label_current = Label(frame_header, font=subtitle_font)
        label_current.place(x=485, y=20)

        # ======Employee ID label======
        label_id = Label(self.window_create, text="Employee ID:")
        label_id.place(x=50, y=120)

        # ======Employee ID entry box======
        entry_id = Entry(self.window_create, width=30)
        entry_id.insert(END, '')
        entry_id.place(x=150, y=120)

        # ======First name label======
        label_first_name = Label(self.window_create, text="First Name:")
        label_first_name.place(x=50, y=200)

        # ======First name entry box======
        entry_first_name = Entry(self.window_create, width=30)
        entry_first_name.insert(END, '')
        entry_first_name.place(x=150, y=200)

        # ======Surname label======
        label_surname = Label(self.window_create, text="Surname:")
        label_surname.place(x=50, y=280)

        # ======Surname entry box======
        entry_surname = Entry(self.window_create, width=30)
        entry_surname.insert(END, '')
        entry_surname.place(x=150, y=280)

        # ======Gender label======
        label_gender = Label(self.window_create, text="Gender:")
        label_gender.place(x=50, y=360)

        # ======Gender radio buttons======
        rb_gender = IntVar()
        rb_gender.set(1)

        radiobutton_male = Radiobutton(self.window_create, text="Male", variable=rb_gender, value=1)
        radiobutton_male.place(x=150, y=360)

        radiobutton_female = Radiobutton(self.window_create, text="Female", variable=rb_gender, value=2)
        radiobutton_female.place(x=260, y=360)

        # ======Department label======
        label_department = Label(self.window_create, text="Department:")
        label_department.place(x=50, y=440)

        # ======Department option menu======
        list_departments = ["Business Development", "Services", "Marketing", "Engineering", "Training", "Legal",
                            "Human Resources", "Sales", "Product Management", "Support", "Product Management"]
        department = StringVar()
        option_menu_department = OptionMenu(self.window_create, department, *list_departments)
        option_menu_department.place(x=150, y=440)

        # ======Position label======
        label_position = Label(self.window_create, text="Position:")
        label_position.place(x=380, y=440)

        # ======Position entry box======
        entry_position = Entry(self.window_create, width=30)
        entry_position.insert(END, '')
        entry_position.place(x=480, y=440)

        # ======Date of birth label======
        label_dob = Label(self.window_create, text="Date of Birth:")
        label_dob.place(x=50, y=520)

        # ======Date of birth date entry======
        date_entry_dob = DateEntry(self.window_create, width=12, borderwidth=2)
        date_entry_dob.place(x=150, y=520)

        # ======Start date label======
        label_start_date = Label(self.window_create, text="Start Date:")
        label_start_date.place(x=380, y=520)

        # ======Start date date entry======
        date_entry_start_date = DateEntry(self.window_create, width=12, borderwidth=2)
        date_entry_start_date.place(x=480, y=520)

        # ======Email label======
        label_email = Label(self.window_create, text="Email:")
        label_email.place(x=50, y=600)

        # ======Email entry box======
        entry_email = Entry(self.window_create, width=30)
        entry_email.insert(END, '')
        entry_email.place(x=150, y=600)

        # ======Contact label======
        label_contact = Label(self.window_create, text="Contact:")
        label_contact.place(x=380, y=600)

        # ======Contact entry box======
        entry_contact = Entry(self.window_create, width=30)
        entry_contact.insert(END, '')
        entry_contact.place(x=480, y=600)

        # ======Salary label======
        label_salary = Label(self.window_create, text="Salary:")
        label_salary.place(x=50, y=640)

        # ======Salary entry box======
        spinbox_salary = Spinbox(self.window_create, from_=0, to=1000000, increment=1000)
        spinbox_salary.place(x=150, y=640)

        # ======Active label======
        label_active = Label(self.window_create, text="Active:")
        label_active.place(x=380, y=640)

        # ======Active radio buttons======
        rb_active = IntVar()
        rb_active.set(1)

        radiobutton_yes = Radiobutton(self.window_create, text="Yes", variable=rb_active, value=1)
        radiobutton_yes.place(x=450, y=640)

        radiobutton_no = Radiobutton(self.window_create, text="No", variable=rb_active, value=2)
        radiobutton_no.place(x=500, y=640)

        # ======Address label======
        label_address = Label(self.window_create, text="Address:")
        label_address.place(x=50, y=720)

        # ======Address label======
        text_address = Text(self.window_create, width=64, height=10)
        text_address.place(x=150, y=720)

        # ======Picture label======
        label_picture = Label(self.window_create, relief="raised")
        label_picture.place(x=460, y=120)

        # ======Add button======
        button_add = Button(self.window_create, text="Add", command=add_to_database)
        button_add.place(x=340, y=900)
