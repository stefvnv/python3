"""
Employee Portal
    instance.py

Stefana Chiritescu
"""

from tkinter import *
from io import BytesIO
from tkinter import messagebox

from PIL import Image, ImageTk
from tkcalendar import DateEntry

from fonts import *
from database import *

# global variables
global parent_update, default_parent_state


class EmployeeDisplayer:

    def __init__(self, parent, parent_update_function, parent_default_entries):
        self.__window_employee = 0
        global parent_update, default_parent_state
        parent_update = parent_update_function
        default_parent_state = parent_default_entries

    @staticmethod
    def read_window(self):
        """Returns current window"""

        return self.window_employee

    @staticmethod
    def display_employee(self, window_portal, emp_data, index):
        """Initializes GUI for managing employee as toplevel"""

        # GUI settings
        self.window_employee = Toplevel(window_portal)
        self.window_employee.geometry("720x1000")
        self.window_employee.title("Employee Portal - Employee Management System | Employee Information")
        self.window_employee.resizable(False, False)
        self.window_employee.config(bg="#B0B6A1", highlightbackground="black", highlightthickness=4)

        # ============ METHODS ============
        def display_instance():
            """Displays instance of employee selected in portal.py"""

            # inserts information of current employee into label, entry boxes, radio buttons, option menu and text box
            # using Employee class read methods
            label_current.config(text="Employee ID: " + emp_data[index].read_id())

            entry_id.delete(0, END)
            entry_id.insert(END, emp_data[index].read_id())
            entry_id.config(state="disabled")

            entry_first_name.delete(0, END)
            entry_first_name.insert(END, emp_data[index].read_first_name())

            entry_surname.delete(0, END)
            entry_surname.insert(END, emp_data[index].read_surname())

            if emp_data[index].read_gender() == "Male":
                rb_gender.set("Male")
            else:
                rb_gender.set("Female")

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

            if emp_data[index].read_active() == 1:
                rb_active.set("Yes")
            else:
                rb_active.set("No")

            text_address.insert(END, emp_data[index].read_address())

            # render and insert image
            img_byte = BytesIO(emp_data[index].read_picture())
            self.window_employee.image = ImageTk.PhotoImage(Image.open(img_byte).resize((200, 250), Image.ANTIALIAS))
            label_picture.config(image=self.window_employee.image)

        def update_employee():
            """Selects current employee from database, gets information from window and updates their
            information in database """

            # global variable
            global parent_update

            cur.execute("SELECT * FROM Employee")

            # gets content from entry fields, radio buttons, date entry, spinbox and text box
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

            cur.execute(
                # [SQL] updates current employee information in database
                "UPDATE Employee SET first_name = (\'" + new_first_name + "\'), surname = (\'" + new_surname + "\'),  gender = (\'" + new_gender + "\'), department = (\'" + new_department + "\'), position = (\'" + new_position + "\'), date_of_birth = (\'" + new_dob + "\'), email = (\'" + new_email + "\'), contact = (\'" + new_contact + "\'), salary = (\'" + new_salary + "\'), active = (\'" + new_active + "\'), address = (\'" + new_address + "\') WHERE emp_id = \'" + entry_id.get() + "\'")
            con.commit()

            # message upon success
            messagebox.showinfo("Employee Updated", "Current employee information was updated successfully.")

            parent_update()
            default_parent_state()

        def delete_employee():
            """Deletes current employee from database"""

            # global variable
            global parent_update

            # [SQL] deletes current employee from database
            cur.execute("DELETE FROM Employee WHERE emp_id = \'" + entry_id.get() + "\'")
            con.commit()

            messagebox.showinfo("Employee Deleted", "Current employee has been deleted from the database successfully.")

            # destroys current window
            self.window_employee.destroy()

            parent_update()
            default_parent_state()

        def on_closing():
            """Destroys current window when window is closed (X)"""
            self.window_employee.destroy()
        self.window_employee.protocol("WM_DELETE_WINDOW", on_closing)

        # ============ GUI ============

        # ======Frame header======
        frame_header = Frame(self.window_employee, width=720, height=60, bg="#182c25")
        frame_header.place(x=0, y=0)

        # ======Title label======
        label_title = Label(frame_header, font=title_font, text="Employee Portal", fg="white", bg="#182c25")
        label_title.place(x=10, y=0)

        # ======Current Employee ID label======
        label_current = Label(frame_header, font=subtitle_font, fg="white", bg="#182c25")
        label_current.place(x=450, y=20)

        # ======Employee ID label======
        label_id = Label(self.window_employee, text="Employee ID", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_id.place(x=40, y=120)

        # ======Employee ID entry box======
        entry_id = Entry(self.window_employee, font=small_font, width=30)
        entry_id.insert(END, '')
        entry_id.place(x=150, y=120)

        # ======First name label======
        label_first_name = Label(self.window_employee, font=body_font, text="First Name", bg="#B0B6A1", fg="#182c25")
        label_first_name.place(x=40, y=200)

        # ======First name entry box======
        entry_first_name = Entry(self.window_employee, font=small_font, width=30)
        entry_first_name.insert(END, '')
        entry_first_name.place(x=150, y=200)

        # ======Surname label======
        label_surname = Label(self.window_employee, font=body_font, text="Surname", bg="#B0B6A1", fg="#182c25")
        label_surname.place(x=40, y=280)

        # ======Surname entry box======
        entry_surname = Entry(self.window_employee, font=small_font, width=30)
        entry_surname.insert(END, '')
        entry_surname.place(x=150, y=280)

        # ======Gender label======
        label_gender = Label(self.window_employee, font=body_font, text="Gender", bg="#B0B6A1", fg="#182c25")
        label_gender.place(x=40, y=360)

        # ======Gender radio buttons======
        rb_gender = StringVar()

        radiobutton_male = Radiobutton(self.window_employee, text="Male", font=small_font, variable=rb_gender,
                                       value="Male", bg="#B0B6A1")
        radiobutton_male.place(x=150, y=360)

        radiobutton_female = Radiobutton(self.window_employee, text="Female", font=small_font, variable=rb_gender,
                                         value="Female", bg="#B0B6A1")
        radiobutton_female.place(x=260, y=360)

        # ======Department label======
        label_department = Label(self.window_employee, text="Department", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_department.place(x=40, y=440)

        # ======Department option menu======
        list_departments = ["Business Development", "Services", "Marketing", "Engineering", "Training", "Legal",
                            "Human Resources", "Sales", "Product Management", "Support", "Product Management"]
        department = StringVar()
        option_menu_department = OptionMenu(self.window_employee, department, *list_departments)
        option_menu_department["menu"].config(font=small_font)
        department.set("Business Development")
        option_menu_department.config(font=small_font)
        option_menu_department.place(x=150, y=440)

        # ======Position label======
        label_position = Label(self.window_employee, font=body_font, text="Position", bg="#B0B6A1", fg="#182c25")
        label_position.place(x=380, y=440)

        # ======Position entry box======
        entry_position = Entry(self.window_employee, width=27, font=small_font)
        entry_position.insert(END, '')
        entry_position.place(x=460, y=440)

        # ======Date of birth label======
        label_dob = Label(self.window_employee, text="Date of Birth", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_dob.place(x=40, y=520)

        # ======Date of birth date entry======
        date_entry_dob = DateEntry(self.window_employee, width=12, borderwidth=2, font=small_font)
        date_entry_dob.place(x=150, y=520)

        # ======Start date label======
        label_start_date = Label(self.window_employee, text="Start Date", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_start_date.place(x=380, y=520)

        # ======Start date date entry======
        date_entry_start_date = DateEntry(self.window_employee, width=12, borderwidth=2, font=small_font)
        date_entry_start_date.place(x=460, y=520)

        # ======Email label======
        label_email = Label(self.window_employee, text="Email", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_email.place(x=40, y=600)

        # ======Email entry box======
        entry_email = Entry(self.window_employee, width=30, font=small_font)
        entry_email.insert(END, '')
        entry_email.place(x=150, y=600)

        # ======Contact label======
        label_contact = Label(self.window_employee, text="Contact", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_contact.place(x=380, y=600)

        # ======Contact entry box======
        entry_contact = Entry(self.window_employee, width=27, font=small_font)
        entry_contact.insert(END, '')
        entry_contact.place(x=460, y=600)

        # ======Salary label======
        label_salary = Label(self.window_employee, text="Salary", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_salary.place(x=40, y=670)

        # ======Salary entry box======
        spinbox_salary = Spinbox(self.window_employee, from_=0, to=1000000, increment=1000, font=small_font)
        spinbox_salary.place(x=150, y=670)

        # ======Active label======
        label_active = Label(self.window_employee, text="Active", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_active.place(x=380, y=670)

        # ======Active radio buttons======
        rb_active = StringVar()

        radiobutton_yes = Radiobutton(self.window_employee, text="Yes", font=small_font, variable=rb_active,
                                      value="Yes", bg="#B0B6A1")
        radiobutton_yes.place(x=460, y=670)

        radiobutton_no = Radiobutton(self.window_employee, text="No", font=small_font, variable=rb_active, value="No",
                                     bg="#B0B6A1")
        radiobutton_no.place(x=570, y=670)

        # ======Address label======
        label_address = Label(self.window_employee, text="Address", font=body_font, bg="#B0B6A1", fg="#182c25")
        label_address.place(x=40, y=740)

        # ======Address text======
        text_address = Text(self.window_employee, width=72, height=6, font=small_font)
        text_address.place(x=150, y=740)

        # ======Picture label======
        label_picture = Label(self.window_employee, relief="raised")
        label_picture.place(x=450, y=120)

        # ======Update button======
        button_update = Button(self.window_employee, text="Update", command=update_employee, width=10, font=12,
                               bg="#1e453e", fg="white", activebackground="#306844")
        button_update.place(x=180, y=900)

        # ======Delete button======
        button_delete = Button(self.window_employee, text="Delete", command=delete_employee, width=10, font=12,
                               bg="#1e453e", fg="white", activebackground="#306844")
        button_delete.place(x=460, y=900)

        # start method
        display_instance()
