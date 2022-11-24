import tkinter
from tkinter import *
from time import strftime
from tkinter import Tk, messagebox
from instance import *
from Employee import *
from io import BytesIO
from PIL import Image, ImageTk
from database import *
from create_employee import *
from fonts import *

# variables
global emp_displayer
global emp_creator
global search
global set_default_entries

emp_list = []
current_index = -1


class Singleton:
    instance = None

    @staticmethod
    def open_instance(window_portal, current, employee_list):
        if Singleton.instance is None:
            if current_index != -1:
                emp_displayer.display_employee(emp_displayer, window_portal, employee_list, current)
                Singleton()
            else:
                messagebox.showwarning("Warning", "An employee must be selected to proceed.")

        else:
            if current_index != -1:
                if not tkinter.Toplevel.winfo_exists(emp_displayer.read_window(emp_displayer)):
                    emp_displayer.display_employee(emp_displayer, window_portal, employee_list, current)
                    Singleton()
                else:
                    messagebox.showwarning("Warning", "An employee is already open.")

    def __init__(self):
        if Singleton.instance is None:
            Singleton.instance = self


class SingletonTwo:
    instance = None

    @staticmethod
    def open_instance(window_portal):
        global search
        if SingletonTwo.instance is None:
            emp_creator.create_employee(emp_creator, window_portal)
            SingletonTwo()
        else:
            if not tkinter.Toplevel.winfo_exists(emp_creator.read_window(emp_creator)):
                emp_creator.create_employee(emp_creator, window_portal)
                SingletonTwo()

    def __init__(self):
        if SingletonTwo.instance is None:
            SingletonTwo.instance = self


def initiate_portal(window):
    """Initiates the GUI"""
    global emp_creator, search, emp_displayer, set_default_entries

    background = PhotoImage(file="images/background_portal.png")

    window_portal = Toplevel(window)
    window_portal.geometry("1280x720")
    window_portal.title("Employee Portal - Employee Management System")
    window_portal.resizable(False, False)

    def live_clock():
        time_string = strftime("%H:%M:%S,\n%A, %d %B")
        label_clock.config(text=time_string)
        label_clock.after(1000, live_clock)

    def set_default_entries():
        entry_search.delete(0, END)
        entry_first_name.delete(0, END)
        entry_surname.delete(0, END)
        entry_position.delete(0, END)
        label_picture.config(image=window_portal.default)

    def search():
        """"""
        global emp_list

        # getting data from database
        cur.execute("SELECT * FROM Employee")

        # database to 2d array
        array_2d = cur.fetchall()

        emp_id_list = []

        emp_list = []
        for emp in array_2d:
            emp_list.append(
                Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10],
                         emp[11], emp[12], emp[13]))

        for emp_id in emp_list:
            emp_id_list.append(emp_id.read_id())

        def update(data_list):
            listbox_id.delete(0, END)

            for item in data_list:
                listbox_id.insert(END, item)

        def fill(e):
            """Populate entry boxes and image label based on ID clicked in listbox"""
            global current_index

            entry_search.delete(0, END)
            entry_search.insert(0, listbox_id.get(ANCHOR))

            for e in range(len(emp_list)):
                if emp_list[e].read_id() == listbox_id.get(ANCHOR):
                    current_index = e

            entry_first_name.delete(0, END)
            entry_first_name.insert(END, emp_list[current_index].read_first_name())

            entry_surname.delete(0, END)
            entry_surname.insert(END, emp_list[current_index].read_surname())

            entry_position.delete(0, END)
            entry_position.insert(END, emp_list[current_index].read_position())

            # render and insert image
            img_byte = BytesIO(emp_list[current_index].read_picture())
            window_portal.image = ImageTk.PhotoImage(Image.open(img_byte).resize((200, 250), Image.ANTIALIAS))
            label_picture.config(image=window_portal.image)

        def check(e):
            typed = entry_search.get()
            if typed == '':
                info = []
                for x in emp_list:
                    info.append(x.read_id())
            else:
                info = []

                for item in emp_id_list:
                    if typed in item:
                        info.append(item)
            update(info)

        update(emp_id_list)

        listbox_id.bind("<<ListboxSelect>>", fill)
        entry_search.bind("<KeyRelease>", check)

    emp_creator = EmployeeCreator(window_portal, search)
    emp_displayer = EmployeeDisplayer(window_portal, search, set_default_entries)

    def logout():
        window_portal.destroy()
        window.deiconify()

    def exit_app():
        window.quit()

    # ============ GUI ============

    # ======Frame Header======
    frame_header = Frame(window_portal, width=1280, height=60, bg="#182c25")
    frame_header.place(x=0, y=0)

    # ======Frame Body======
    frame_body = Frame(window_portal, width=1280, height=660)
    frame_body.place(x=0, y=60)

    # ====== Canvas ======
    canvas = Canvas(frame_body, width=1280, height=660, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # ====== Set Background image ======
    canvas.create_image(0, 0, image=background, anchor="nw")

    # ======Title label======
    label_title = Label(frame_header, text="Employee Portal - Dashboard", font=header_font, bg="#182c25", fg="white")
    label_title.place(x=5, y=0)

    # ======Live clock label======
    label_clock = Label(frame_header, font=subtitle_font, bg="#182c25", fg="white")
    label_clock.place(x=1000, y=0)

    # ======View employee button======
    button_view_employee = Button(window_portal, text="Manage Employee", font="body_font", width=30, bg="#22311d",
                                  fg="white",
                                  command=lambda: Singleton.open_instance(window_portal, current_index, emp_list))
    button_view_employee.place(x=20, y=80)

    # ======Add new employee button======
    button_add = Button(window_portal, text="Add Employee", font="body_font", width=30, bg="#22311d", fg="white",
                        command=lambda: SingletonTwo.open_instance(window_portal))
    button_add.place(x=340, y=80)

    # ======Log out button======
    button_log_out = Button(window_portal, text="Logout", font="body_font", width=30, bg="#22311d", fg="white",
                            command=logout)
    button_log_out.place(x=660, y=80)

    # ======Exit button======
    button_exit = Button(window_portal, text="Exit", font="body_font", width=30, bg="#22311d", fg="white",
                         command=exit_app)
    button_exit.place(x=980, y=80)

    # ======Search Employee label======
    label_id = Label(window_portal, text="Search (by ID)", font="body_font")
    label_id.place(x=100, y=200)

    # ======Search entry box======
    entry_search = Entry(window_portal, width=30, font="body_font")
    entry_search.insert(END, '')
    entry_search.focus_set()
    entry_search.place(x=300, y=200)

    # ======Employee ID listbox======
    listbox_id = Listbox(window_portal, width=30, height=20, font="body_font")
    listbox_id.place(x=300, y=250)

    # ======First name label======
    label_first_name = Label(window_portal, text="First Name", font="body_font")
    label_first_name.place(x=600, y=500)

    # ======First name entry box======
    entry_first_name = Entry(window_portal, width=20, font="body_font")
    entry_first_name.insert(END, '')
    entry_first_name.place(x=700, y=500)

    # ======Surname label======
    label_surname = Label(window_portal, text="Surname", font="body_font")
    label_surname.place(x=600, y=550)

    # ======Surname entry box======
    entry_surname = Entry(window_portal, width=20, font="body_font")
    entry_surname.insert(END, '')
    entry_surname.place(x=700, y=550)

    # ======Position label======
    label_position = Label(window_portal, text="Position", font="body_font")
    label_position.place(x=600, y=610)

    # ======Position entry box======
    entry_position = Entry(window_portal, width=20, font="body_font")
    entry_position.insert(END, '')
    entry_position.place(x=700, y=610)

    # ======Picture label======
    window_portal.default = PhotoImage(file="./images/user.png")

    label_picture = Label(window_portal, relief="raised", width=200, height=250, image=window_portal.default)
    label_picture.place(x=700, y=200)

    # start methods
    search()
    live_clock()
