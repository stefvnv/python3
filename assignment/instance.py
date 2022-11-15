from tkinter import *
from io import BytesIO
from tkinter import messagebox

from PIL import Image, ImageTk
from tkcalendar import DateEntry

from fonts import *


class EmployeeDisplayer:

    def __init__(self):
        self.__window_employee = 0

    @staticmethod
    def read_window(self):
        return self.window_employee

    @staticmethod
    def display_employee(self, window_portal, emp_data, index):
        self.window_employee = Toplevel(window_portal)
        self.window_employee.geometry("720x1000")
        self.window_employee.title("Employee Portal - Employee Management System | Employee Information")
        self.window_employee.resizable(False, False)
        self.window_employee.config(bg="#B0B6A1")

        # ============ METHODS ============
        def display_instance():
            label_current.config(text="Employee ID: " + emp_data[index].read_id())

            entry_id.delete(0, END)
            entry_id.insert(END, emp_data[index].read_id())

            entry_first_name.delete(0, END)
            entry_first_name.insert(END, emp_data[index].read_first_name())

            entry_surname.delete(0, END)
            entry_surname.insert(END, emp_data[index].read_surname())

            # fix - not to update everything (separate method)
            if emp_data[index].read_gender() == "Male":
                rb_gender.set(1)
            else:
                rb_gender.set(2)

            # to do department
            if emp_data[index].read_department() == "Business Development":
                department.set("Business Development")
            elif emp_data[index].read_department() == "Services":
                department.set("Services")
            elif emp_data[index].read_department() == "Marketing":
                department.set("Marketing")
            elif emp_data[index].read_department() == "Engineering":
                department.set("Engineering")
            elif emp_data[index].read_department() == "Training":
                department.set("Training")
            elif emp_data[index].read_department() == "Legal":
                department.set("Legal")
            elif emp_data[index].read_department() == "Human Resources":
                department.set("Human Resources")
            elif emp_data[index].read_department() == "Product Management":
                department.set("Product Management")
            elif emp_data[index].read_department() == "Support":
                department.set("Support")
            elif emp_data[index].read_department() == "Product Management":
                department.set("Product Management")

            entry_position.delete(0, END)
            entry_position.insert(END, emp_data[index].read_position())

            date_entry_dob.delete(0, END)
            date_entry_dob.insert(END, emp_data[index].read_dob())

            date_entry_start_date.delete(0, END)
            date_entry_start_date.insert(END, emp_data[index].read_start_date())

            entry_email.delete(0, END)
            entry_email.insert(END, emp_data[index].read_email())

            entry_contact.delete(0, END)
            entry_contact.insert(END, emp_data[index].read_contact())

            spinbox_salary.delete(0, END)
            spinbox_salary.insert(END, emp_data[index].read_salary())

            # fix - not to update everything (separate method)
            if emp_data[index].read_active():
                rb_active.set(1)
            else:
                rb_active.set(2)

            text_address.insert(END, emp_data[index].read_address())

            # render and insert image
            img_byte = BytesIO(emp_data[index].read_picture())
            self.window_employee.image = ImageTk.PhotoImage(Image.open(img_byte).resize((200, 250), Image.ANTIALIAS))
            label_picture.config(image=self.window_employee.image)

        # def update_employee():

        # def delete_employee():

        def on_closing():
            self.window_employee.destroy()

        self.window_employee.protocol("WM_DELETE_WINDOW", on_closing)

        # ============ GUI ============

        # ======Frame header======
        frame_header = Frame(self.window_employee, width=720, height=60, bg="red")
        frame_header.place(x=0, y=0)

        # ======Title label======
        label_title = Label(frame_header, font=title_font, text="Employee Portal")
        label_title.place(x=10, y=0)

        # ======Current Employee ID label======
        label_current = Label(frame_header, font=subtitle_font)
        label_current.place(x=485, y=20)

        # ======Employee ID label======
        label_id = Label(self.window_employee, text="Employee ID:")
        label_id.place(x=50, y=120)

        # ======Employee ID entry box======
        entry_id = Entry(self.window_employee, width=30)
        entry_id.insert(END, '')
        entry_id.place(x=150, y=120)

        # ======First name label======
        label_first_name = Label(self.window_employee, text="First Name:")
        label_first_name.place(x=50, y=200)

        # ======First name entry box======
        entry_first_name = Entry(self.window_employee, width=30)
        entry_first_name.insert(END, '')
        entry_first_name.place(x=150, y=200)

        # ======Surname label======
        label_surname = Label(self.window_employee, text="Surname:")
        label_surname.place(x=50, y=280)

        # ======Surname entry box======
        entry_surname = Entry(self.window_employee, width=30)
        entry_surname.insert(END, '')
        entry_surname.place(x=150, y=280)

        # ======Gender label======
        label_gender = Label(self.window_employee, text="Gender:")
        label_gender.place(x=50, y=360)

        # ======Gender radio buttons======
        rb_gender = IntVar()

        radiobutton_male = Radiobutton(self.window_employee, text="Male", variable=rb_gender, value=1,
                                       command=display_instance)
        radiobutton_male.place(x=150, y=360)

        radiobutton_female = Radiobutton(self.window_employee, text="Female", variable=rb_gender, value=2,
                                         command=display_instance)
        radiobutton_female.place(x=260, y=360)

        # ======Department label======
        label_surname = Label(self.window_employee, text="Department:")
        label_surname.place(x=50, y=440)

        # ======Department option menu======
        list_departments = ["Business Development", "Services", "Marketing", "Engineering", "Training", "Legal",
                            "Human Resources", "Sales", "Product Management", "Support", "Product Management"]
        department = StringVar()
        option_menu_department = OptionMenu(self.window_employee, department, *list_departments)
        option_menu_department.place(x=150, y=440)

        # ======Position label======
        label_position = Label(self.window_employee, text="Position:")
        label_position.place(x=380, y=440)

        # ======Position entry box======
        entry_position = Entry(self.window_employee, width=30)
        entry_position.insert(END, '')
        entry_position.place(x=480, y=440)

        # ======Date of birth label======
        label_dob = Label(self.window_employee, text="Date of Birth:")
        label_dob.place(x=50, y=520)

        # ======Date of birth date entry======
        date_entry_dob = DateEntry(self.window_employee, width=12, borderwidth=2)
        date_entry_dob.place(x=150, y=520)

        # ======Start date label======
        label_start_date = Label(self.window_employee, text="Start Date:")
        label_start_date.place(x=380, y=520)

        # ======Start date date entry======
        date_entry_start_date = DateEntry(self.window_employee, width=12, borderwidth=2)
        date_entry_start_date.place(x=480, y=520)

        # ======Email label======
        label_email = Label(self.window_employee, text="Email:")
        label_email.place(x=50, y=600)

        # ======Email entry box======
        entry_email = Entry(self.window_employee, width=30)
        entry_email.insert(END, '')
        entry_email.place(x=150, y=600)

        # ======Contact label======
        label_contact = Label(self.window_employee, text="Contact:")
        label_contact.place(x=380, y=600)

        # ======Contact entry box======
        entry_contact = Entry(self.window_employee, width=30)
        entry_contact.insert(END, '')
        entry_contact.place(x=480, y=600)

        # ======Salary label======
        label_salary = Label(self.window_employee, text="Salary:")
        label_salary.place(x=50, y=640)

        # ======Salary entry box======
        spinbox_salary = Spinbox(self.window_employee, from_=0, to=1000000, increment=1000)
        spinbox_salary.place(x=150, y=640)

        # ======Active label======
        label_active = Label(self.window_employee, text="Active:")
        label_active.place(x=380, y=640)

        # ======Active radio buttons======
        rb_active = IntVar()

        radiobutton_yes = Radiobutton(self.window_employee, text="Yes", variable=rb_active, value=1,
                                      command=display_instance)
        radiobutton_yes.place(x=450, y=640)

        radiobutton_no = Radiobutton(self.window_employee, text="No", variable=rb_active, value=2, command=display_instance)
        radiobutton_no.place(x=500, y=640)

        # ======Address label======
        label_address = Label(self.window_employee, text="Address:")
        label_address.place(x=50, y=720)

        # ======Address label======
        text_address = Text(self.window_employee, width=64, height=10)
        text_address.place(x=150, y=720)

        # ======Picture label======
        label_picture = Label(self.window_employee, relief="raised")
        label_picture.place(x=460, y=120)

        # ======Update button======
        button_update = Button(self.window_employee, text="Update")
        button_update.place(x=200, y=900)

        # ======Delete button======
        button_delete = Button(self.window_employee, text="Delete")
        button_delete.place(x=480, y=900)

        display_instance()
