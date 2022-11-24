"""
Employee Portal
    create_employee.py

Stefana Chiritescu
"""

import random

from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkcalendar import DateEntry

from fonts import *
from database import *

# global variables
global parent_search
global blob_data
global new_picture


class EmployeeCreator:

    def __init__(self, parent_in, parent_update):
        global parent_search
        self.__window_create = 0
        parent_search = parent_update

    @staticmethod
    def read_window(self):
        """Returns current window"""

        return self.window_create

    @staticmethod
    def create_employee(self, window_portal):
        """Initializes GUI for adding new employee as toplevel"""

        # GUI settings
        self.window_create = Toplevel(window_portal)
        self.window_create.geometry("720x1000")
        self.window_create.title("Employee Portal - Employee Management System | Add New Employee")
        self.window_create.resizable(False, False)
        self.window_create.config(bg="#B0B6A1", highlightbackground="black", highlightthickness=4)

        # ============ METHODS ============
        def display_id():
            """Inserts random number in ID entry field"""

            fixed_digits = 4
            random_id = str(random.randrange(1000, 9999, fixed_digits))

            entry_id.insert(END, random_id)
            entry_id.config(state="disabled")

        def add_to_database():
            """Gets information from window and inserts to database table as new employee"""

            # global variables
            global parent_search, blob_data, new_picture

            # gets content from entry fields, radio buttons, date entry, spinbox and text box
            new_id = entry_id.get()
            new_first_name = entry_first_name.get()
            new_surname = entry_surname.get()
            new_gender = rb_gender.get()
            new_department = department.get()
            new_position = entry_position.get()
            new_dob = date_entry_dob.get()
            new_start_date = date_entry_start_date.get()
            new_email = entry_email.get()
            new_contact = entry_contact.get()
            new_salary = spinbox_salary.get()
            new_active = rb_active.get()
            new_address = text_address.get("1.0", END)

            try:
                new_picture = blob_data

                # stores information in new employee array
                new_employee = [
                    (new_id, new_first_name, new_surname, new_gender, new_department, new_position, new_dob,
                     new_start_date, new_email, new_contact, new_salary, new_active, new_address, new_picture)]

                try:
                    # [SQL] inserts new employee array into database
                    cur.executemany("INSERT into Employee VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", new_employee)
                except sqlite3.IntegrityError:
                    messagebox.showinfo("Error", "ID Must be unique")
                else:
                    messagebox.showinfo("Employee Added", "Employee added to database successfully.")
                    on_closing()

            except NameError:
                messagebox.showinfo("Error", "Must add a picture")

            con.commit()
            parent_search()

        def on_closing():
            """Destroys current window when window is closed (X)"""

            self.window_create.destroy()
        self.window_create.protocol("WM_DELETE_WINDOW", on_closing)

        def upload_img():
            """Opens file explorer to select image, resizes and inserts it into label"""

            # global image
            global blob_data

            # accept jpg files only
            f_types = [('Jpg Files', '*.jpg')]

            # store image selected from file explorer into filename
            filename = filedialog.askopenfilename(filetypes=f_types)
            blob_data = filename

            # render and insert image
            self.window_create.image = ImageTk.PhotoImage(Image.open(filename).resize((200, 250), Image.ANTIALIAS))
            label_picture.config(image=self.window_create.image, width=200, height=250)

        # ============ GUI ============

        # ======Frame header======
        frame_header = Frame(self.window_create, width=720, height=60, bg="#182c25")
        frame_header.place(x=0, y=0)

        # ======Title label======
        label_title = Label(frame_header, font=title_font, text="Employee Portal", fg="white", bg="#182c25")
        label_title.place(x=10, y=0)

        # ======Add New Employee label======
        label_new = Label(frame_header, font=subtitle_font, text="Add New Employee", fg="white", bg="#182c25")
        label_new.place(x=440, y=20)

        # ======Employee ID label======
        label_id = Label(self.window_create, text="Employee ID", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_id.place(x=50, y=120)

        # ======Employee ID entry box======
        entry_id = Entry(self.window_create, font=small_font, width=30)
        entry_id.insert(END, '')
        entry_id.place(x=150, y=120)

        # ======First name label======
        label_first_name = Label(self.window_create, font=body_font, text="First Name", bg="#B0B6A1", fg="#182c25")
        label_first_name.place(x=50, y=200)

        # ======First name entry box======
        entry_first_name = Entry(self.window_create, font=small_font, width=30)
        entry_first_name.insert(END, '')
        entry_first_name.place(x=150, y=200)

        # ======Surname label======
        label_surname = Label(self.window_create, font=body_font, text="Surname", bg="#B0B6A1", fg="#182c25")
        label_surname.place(x=50, y=280)

        # ======Surname entry box======
        entry_surname = Entry(self.window_create, font=small_font, width=30)
        entry_surname.insert(END, '')
        entry_surname.place(x=150, y=280)

        # ======Gender label======
        label_gender = Label(self.window_create, font=body_font, text="Gender", bg="#B0B6A1", fg="#182c25")
        label_gender.place(x=50, y=360)

        # ======Gender radio buttons======
        rb_gender = IntVar()
        rb_gender.set(1)

        radiobutton_male = Radiobutton(self.window_create, text="Male", font=small_font, variable=rb_gender, value=1,
                                       bg="#B0B6A1")
        radiobutton_male.place(x=150, y=360)

        radiobutton_female = Radiobutton(self.window_create, text="Female", font=small_font, variable=rb_gender,
                                         value=2, bg="#B0B6A1")
        radiobutton_female.place(x=260, y=360)

        # ======Department label======
        label_department = Label(self.window_create, text="Department", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_department.place(x=50, y=440)

        # ======Department option menu======
        list_departments = ["Business Development", "Services", "Marketing", "Engineering", "Training", "Legal",
                            "Human Resources", "Sales", "Product Management", "Support", "Product Management"]
        department = StringVar()
        option_menu_department = OptionMenu(self.window_create, department, *list_departments)
        option_menu_department["menu"].config(font=small_font)
        department.set("Business Development")
        option_menu_department.config(font=small_font)
        option_menu_department.place(x=150, y=440)

        # ======Position label======
        label_position = Label(self.window_create, font=body_font, text="Position", bg="#B0B6A1", fg="#182c25")
        label_position.place(x=380, y=440)

        # ======Position entry box======
        entry_position = Entry(self.window_create, width=27, font=small_font)
        entry_position.insert(END, '')
        entry_position.place(x=460, y=440)

        # ======Date of birth label======
        label_dob = Label(self.window_create, text="Date of Birth", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_dob.place(x=40, y=520)

        # ======Date of birth date entry======
        date_entry_dob = DateEntry(self.window_create, width=12, borderwidth=2, font=small_font)
        date_entry_dob.place(x=150, y=520)

        # ======Start date label======
        label_start_date = Label(self.window_create, text="Start Date", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_start_date.place(x=380, y=520)

        # ======Start date date entry======
        date_entry_start_date = DateEntry(self.window_create, width=12, borderwidth=2, font=small_font)
        date_entry_start_date.place(x=460, y=520)

        # ======Email label======
        label_email = Label(self.window_create, text="Email", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_email.place(x=40, y=600)

        # ======Email entry box======
        entry_email = Entry(self.window_create, width=30, font=small_font)
        entry_email.insert(END, '')
        entry_email.place(x=150, y=600)

        # ======Contact label======
        label_contact = Label(self.window_create, text="Contact", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_contact.place(x=380, y=600)

        # ======Contact entry box======
        entry_contact = Entry(self.window_create, width=27, font=small_font)
        entry_contact.insert(END, '')
        entry_contact.place(x=460, y=600)

        # ======Salary label======
        label_salary = Label(self.window_create, text="Salary", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_salary.place(x=40, y=670)

        # ======Salary entry box======
        spinbox_salary = Spinbox(self.window_create, from_=0, to=1000000, increment=1000, font=small_font)
        spinbox_salary.place(x=150, y=670)

        # ======Active label======
        label_active = Label(self.window_create, text="Active", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_active.place(x=380, y=670)

        # ======Active radio buttons======
        rb_active = IntVar()
        rb_active.set(1)

        radiobutton_yes = Radiobutton(self.window_create, text="Yes", variable=rb_active, value=1, bg="#B0B6A1")
        radiobutton_yes.place(x=460, y=670)

        radiobutton_no = Radiobutton(self.window_create, text="No", variable=rb_active, value=2, bg="#B0B6A1")
        radiobutton_no.place(x=570, y=670)

        # ======Address label======
        label_address = Label(self.window_create, text="Address", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_address.place(x=40, y=740)

        # ======Address label======
        text_address = Text(self.window_create, width=72, height=6, font=small_font)
        text_address.place(x=150, y=740)

        # ======Picture label======
        self.window_create.image = PhotoImage(file="./images/user.png")

        label_picture = Label(self.window_create, relief="raised", image=self.window_create.image)
        label_picture.place(x=450, y=120)

        # ======Browse button======
        button_browse = Button(self.window_create, text="Browse", command=upload_img, width=10, bg="#1e453e",
                               fg="white", activebackground="#306844")
        button_browse.place(x=510, y=380)

        # ======Add button======
        button_add = Button(self.window_create, text="Add", command=add_to_database, width=10, font=12, bg="#1e453e",
                            fg="white", activebackground="#306844")
        button_add.place(x=320, y=900)

        # start method
        display_id()
