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

# variables
current_index = -1
emp_list = []
emp_displayer = EmployeeDisplayer()
emp_creator = EmployeeCreator()


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


# ADD ALL GUI STUFF INSIDE THIS METHOD
def initiate_portal(window):
    """Initiates the GUI"""

    window_portal = Toplevel(window)
    window_portal.geometry("1280x720")
    window_portal.title("Employee Portal - Employee Management System")
    window_portal.resizable(False, False)

    def live_clock():
        time_string = strftime("%A, %d %B, %H:%M:%S %p")
        label_clock.config(text=time_string)
        label_clock.after(1000, live_clock)

    def search():
        """"""
        global emp_list

        cur.execute("SELECT * FROM Employee")
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

            # tkinter.Toplevel.winfo_exists(window_portal)

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

    def logout():
        # emp_id_list = []
        window_portal.destroy()
        window.deiconify()

    # fix - click log out and delete old info
    # window_portal.destroy()
    # window_portal.update()

    def exit_app():
        window.quit()

    # ============ GUI ============

    # ======Frame Header======
    frame_header = Frame(window_portal, width=1280, height=60, bg="red")
    frame_header.place(x=0, y=0)

    # ======Live clock======
    label_clock = Label(frame_header)
    label_clock.place(x=1000, y=10)

    # ======Title label======
    label_title = Label(frame_header, font=header_font, text="Employee Portal - Dashboard")
    label_title.place(x=10, y=10)

    # ======Search Employee label======
    label_id = Label(window_portal, text="Search (by Employee ID)")
    label_id.place(x=100, y=80)

    # ======Search entry box======
    entry_search = Entry(window_portal, width=40)
    entry_search.insert(END, '')
    entry_search.focus_set()
    entry_search.place(x=300, y=80)

    # ======Employee ID listbox======
    listbox_id = Listbox(window_portal, width=40, height=5)
    listbox_id.place(x=300, y=120)

    # ======First name label======
    label_first_name = Label(window_portal, text="First Name")
    label_first_name.place(x=100, y=240)

    # ======First name entry box======
    entry_first_name = Entry(window_portal, width=40)
    entry_first_name.insert(END, '')
    entry_first_name.place(x=300, y=240)

    # ======Surname label======
    label_surname = Label(window_portal, text="Surname")
    label_surname.place(x=100, y=320)

    # ======Surname entry box======
    entry_surname = Entry(window_portal, width=40)
    entry_surname.insert(END, '')
    entry_surname.place(x=300, y=320)

    # ======Position label======
    label_position = Label(window_portal, text="Position")
    label_position.place(x=100, y=400)

    # ======Position entry box======
    entry_position = Entry(window_portal, width=40)
    entry_position.insert(END, '')
    entry_position.place(x=300, y=400)

    # ======Picture label======
    label_picture = Label(window_portal, borderwidth=4, relief="solid")
    label_picture.place(x=600, y=200)

    # ======View employee button======
    button_view_employee = Button(window_portal, text="View/Edit Full Employee Profile",
                                  command=lambda: Singleton.open_instance(window_portal, current_index, emp_list))
    button_view_employee.place(x=200, y=600)

    # ======Add new employee button======
    button_add = Button(window_portal, text="Add New Employee",
                        command=lambda: SingletonTwo.open_instance(window_portal))
    button_add.place(x=400, y=600)

    # ======Log out button======
    button_log_out = Button(window_portal, text="Log out", command=logout)
    button_log_out.place(x=600, y=600)

    # ======Exit button======
    button_exit = Button(window_portal, text="Exit", command=exit_app)
    button_exit.place(x=800, y=600)

    # start methods
    search()
    live_clock()
