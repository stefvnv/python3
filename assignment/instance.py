from tkinter import *
from io import BytesIO

from PIL import Image, ImageTk


def display_employee(window_portal, emp_data, index):
    window_employee = Toplevel(window_portal)
    window_employee.geometry("720x1000")
    window_employee.title("Employee Portal - Employee Management System | Employee Information")
    window_employee.resizable(False, False)

    # ============ METHODS ============
    def display_instance():
        label_current.config(text="Employee ID: " + emp_data[index].read_id())

        entry_id.delete(0, END)
        entry_id.insert(END, emp_data[index].read_id())

        entry_first_name.delete(0, END)
        entry_first_name.insert(END, emp_data[index].read_first_name())

        entry_surname.delete(0, END)
        entry_surname.insert(END, emp_data[index].read_surname())

        # to do gender

        # to do department

        entry_position.delete(0, END)
        entry_position.insert(END, emp_data[index].read_position())

        # to do date of birth

        # to do start date

        entry_email.delete(0, END)
        entry_email.insert(END, emp_data[index].read_email())

        spinbox_salary.delete(0, END)
        spinbox_salary.insert(END, emp_data[index].read_salary())

        #text_address.delete(0, END)
        text_address.insert(END, emp_data[index].read_address())

        # to do active radiobutton

        # render and insert image
        img_byte = BytesIO(emp_data[index].read_picture())
        window_employee.image = ImageTk.PhotoImage(Image.open(img_byte).resize((200, 250), Image.ANTIALIAS))
        label_picture.config(image=window_employee.image)

    # def update_employee():

    # def delete_employee():

    # ============ GUI ============

    # ======Frame header======
    frame_header = Frame(window_employee, width=720, height=60, bg="red")
    frame_header.place(x=0, y=0)

    # ======Title label======
    label_title = Label(frame_header, text="Employee Portal")
    label_title.place(x=10, y=10)

    # ======Current Employee ID label======
    label_current = Label(frame_header, text="")
    label_current.place(x=500, y=10)

    # ======Employee ID label======
    label_id = Label(window_employee, text="Employee ID:")
    label_id.place(x=50, y=120)

    # ======Employee ID entry box======
    entry_id = Entry(window_employee, width=30)
    entry_id.insert(END, '')
    entry_id.place(x=150, y=120)

    # ======First name label======
    label_first_name = Label(window_employee, text="First Name:")
    label_first_name.place(x=50, y=200)

    # ======First name entry box======
    entry_first_name = Entry(window_employee, width=30)
    entry_first_name.insert(END, '')
    entry_first_name.place(x=150, y=200)

    # ======Surname label======
    label_surname = Label(window_employee, text="Surname:")
    label_surname.place(x=50, y=280)

    # ======Surname entry box======
    entry_surname = Entry(window_employee, width=30)
    entry_surname.insert(END, '')
    entry_surname.place(x=150, y=280)

    # ======Gender label======
    label_gender = Label(window_employee, text="Gender:")
    label_gender.place(x=50, y=360)

    # ======Gender radio buttons======
    rb = IntVar()
    rb.set(1)

    radiobutton_male = Radiobutton(window_employee, text="Male", variable=rb, value=1)
    radiobutton_male.place(x=150, y=360)

    radiobutton_female = Radiobutton(window_employee, text="Female", variable=rb, value=2)
    radiobutton_female.place(x=260, y=360)

    # PLACE FOR IMAGE HERE

    # ======Department label======
    label_surname = Label(window_employee, text="Department:")
    label_surname.place(x=50, y=440)

    # ======Department option menu======
    list_departments = ["Hello", "Temporary", "Values", "Here"]
    department = StringVar()
    department.set("Hello")
    option_menu_department = OptionMenu(window_employee, department, *list_departments)
    option_menu_department.place(x=150, y=440)

    # ======Position label======
    label_position = Label(window_employee, text="Position:")
    label_position.place(x=380, y=440)

    # ======Position entry box======
    entry_position = Entry(window_employee, width=30)
    entry_position.insert(END, '')
    entry_position.place(x=480, y=440)

    # ======Date of birth label======
    label_dob = Label(window_employee, text="Date of Birth:")
    label_dob.place(x=50, y=520)

    # ======Date of birth entry box======
    entry_dob = Entry(window_employee, width=30)
    entry_dob.insert(END, '')
    entry_dob.place(x=150, y=520)

    # ======Start date label======
    label_start_date = Label(window_employee, text="Start Date:")
    label_start_date.place(x=380, y=520)

    # ======Start date entry box======
    label_start_date = Entry(window_employee, width=30)
    label_start_date.insert(END, '')
    label_start_date.place(x=480, y=520)

    # ======Email label======
    label_email = Label(window_employee, text="Email:")
    label_email.place(x=50, y=600)

    # ======Email entry box======
    entry_email = Entry(window_employee, width=30)
    entry_email.insert(END, '')
    entry_email.place(x=150, y=600)

    # ======Contact label======
    label_contact = Label(window_employee, text="Contact:")
    label_contact.place(x=380, y=600)

    # ======Contact entry box======
    label_contact = Entry(window_employee, width=30)
    label_contact.insert(END, '')
    label_contact.place(x=480, y=600)

    # ======Salary label======
    label_salary = Label(window_employee, text="Salary:")
    label_salary.place(x=50, y=640)

    # ======Salary entry box======
    spinbox_salary = Spinbox(window_employee, from_=0, to=1000000, increment=1000)
    spinbox_salary.place(x=150, y=640)

    # ======Active label======
    label_active = Label(window_employee, text="Active:")
    label_active.place(x=380, y=640)

    # ======Active entry box======
    entry_active = Entry(window_employee, width=30)
    entry_active.insert(END, '')
    entry_active.place(x=480, y=640)

    # ======Address label======
    label_address = Label(window_employee, text="Address:")
    label_address.place(x=50, y=720)

    # ======Address label======
    text_address = Text(window_employee, width=64, height=10)
    text_address.place(x=150, y=720)

    # ======Picture label======
    label_picture = Label(window_employee, borderwidth=4, relief="solid")
    label_picture.place(x=500, y=120)

    # ======Update button======
    button_update = Button(window_employee, text="Update")
    button_update.place(x=200, y=900)

    # ======Delete button======
    button_delete = Button(window_employee, text="Delete")
    button_delete.place(x=480, y=900)

    display_instance()
