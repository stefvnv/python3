"""
Employee Portal
    portal.py

Stefana Chiritescu
"""

import tkinter

from time import strftime
from instance import *
from Employee import *
from io import BytesIO
from create_employee import *
from fonts import *

# global variables
global emp_displayer
global emp_creator
global search
global set_default_entries

current_index = -1
emp_list = []


class Singleton:
    instance = None

    @staticmethod
    def open_instance(window_portal, current, employee_list):
        """Opens one Singleton instance of current employee window"""

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
        """Opens one Singleton instance of new employee window"""

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


class Portal:
    def __init__(self):
        self.__window_create = 0

    @staticmethod
    def read_window(self):
        """Returns current window"""

        return self.window_create

    @staticmethod
    def initiate_portal(self, window):
        """Initiates the Employee Portal GUI"""

        # global variables
        global emp_creator, search, emp_displayer, set_default_entries

        # GUI settings
        self.window_portal = Toplevel(window)
        self.window_portal.geometry("1280x720")
        self.window_portal.title("Employee Portal - Employee Management System")
        self.window_portal.resizable(False, False)

        self.background = PhotoImage(file="images/background_portal.png")

        def live_clock():
            """Gets current time and date, stores in label and refreshes every 1000ms"""

            time_string = strftime("%H:%M:%S,\n%A, %d %B")
            label_clock.config(text=time_string)
            label_clock.after(1000, live_clock)

        def set_default_entries():
            """Deletes content from entry boxes and sets picture label to default user image"""

            entry_search.delete(0, END)
            entry_first_name.config(state="normal")
            entry_first_name.delete(0, END)
            entry_first_name.config(state="disabled")

            entry_surname.config(state="normal")
            entry_surname.delete(0, END)
            entry_surname.config(state="disabled")

            entry_position.config(state="normal")
            entry_position.delete(0, END)
            entry_position.config(state="disabled")

            label_picture.config(image=self.window_portal.default)

        def search():
            """Updates what listbox displays from what is searched on key release"""

            # global variable
            global emp_list

            # get all data from database
            cur.execute("SELECT * FROM Employee")

            # database stored in 2d array
            array_2d = cur.fetchall()

            emp_id_list = []
            emp_list = []

            # creates a list of employees from database entries
            for emp in array_2d:
                emp_list.append(
                    Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10],
                             emp[11], emp[12], emp[13]))

            # creates a list of employee ids
            for emp_id in emp_list:
                emp_id_list.append(emp_id.read_id())

            def update(data_list):
                """Updates listbox to what is in data list"""

                listbox_id.delete(0, END)

                for item in data_list:
                    listbox_id.insert(END, item)

            def fill(e):
                """Populate entry boxes and image label based on ID clicked in listbox"""

                # global variable
                global current_index

                entry_search.delete(0, END)
                entry_search.insert(0, listbox_id.get(ANCHOR))

                for e in range(len(emp_list)):
                    if emp_list[e].read_id() == listbox_id.get(ANCHOR):
                        current_index = e

                entry_first_name.config(state="normal")
                entry_first_name.delete(0, END)
                entry_first_name.insert(END, emp_list[current_index].read_first_name())
                entry_first_name.config(state="disabled")

                entry_surname.config(state="normal")
                entry_surname.delete(0, END)
                entry_surname.insert(END, emp_list[current_index].read_surname())
                entry_surname.config(state="disabled")

                entry_position.config(state="normal")
                entry_position.delete(0, END)
                entry_position.insert(END, emp_list[current_index].read_position())
                entry_position.config(state="disabled")

                # render and insert image
                img_byte = BytesIO(emp_list[current_index].read_picture())
                self.window_portal.image = ImageTk.PhotoImage(Image.open(img_byte).resize((200, 250), Image.ANTIALIAS))
                label_picture.config(image=self.window_portal.image)

            def check(e):
                """Checks if entry search content matches employee IDs and updates list"""

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

        emp_creator = EmployeeCreator(self.window_portal, search)
        emp_displayer = EmployeeDisplayer(self.window_portal, search, set_default_entries)

        def logout():
            """Destroys current window and opens login page"""

            self.window_portal.destroy()
            window.deiconify()

        def exit_app():
            """Quits application"""

            window.quit()

        # ============ GUI ============

        # ======Frame Header======
        frame_header = Frame(self.window_portal, width=1280, height=60, bg="#182c25")
        frame_header.place(x=0, y=0)

        frame_body = Frame(self.window_portal, width=1280, height=600, bg="red")
        frame_body.place(x=0, y=60)

        # ======Canvas======
        canvas = Canvas(frame_body, width=1280, height=660, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background, anchor="nw")

        # ======Title label======
        label_title = Label(frame_header, text="Employee Portal - Dashboard", font=header_font, bg="#182c25",
                            fg="white")
        label_title.place(x=5, y=0)

        # ======Live clock label======
        label_clock = Label(frame_header, font=subtitle_font, bg="#182c25", fg="white")
        label_clock.place(x=980, y=0)

        # ======View employee button======
        button_view_employee = Button(self.window_portal, text="Manage Employee", font=12, width=30,
                                      bg="#1e453e", fg="white", activebackground="#306844",
                                      command=lambda: Singleton.open_instance(self.window_portal, current_index,
                                                                              emp_list))
        button_view_employee.place(x=20, y=80)

        # ======Add new employee button======
        button_add = Button(self.window_portal, text="Add Employee", font=12, width=30, bg="#1e453e",
                            fg="white", activebackground="#306844",
                            command=lambda: SingletonTwo.open_instance(self.window_portal))
        button_add.place(x=340, y=80)

        # ======Log out button======
        button_log_out = Button(self.window_portal, text="Logout", font=12, width=30, bg="#1e453e", fg="white",
                                activebackground="#306844", command=logout)
        button_log_out.place(x=660, y=80)

        # ======Exit button======
        button_exit = Button(self.window_portal, text="Exit", font=12, width=30, bg="#1e453e", fg="white",
                             activebackground="#990000", command=exit_app)
        button_exit.place(x=980, y=80)

        # ======Search Employee text======
        canvas.create_text(230, 150, text="Search by ID", font=("Century Gothic", 12, 'bold'), fill="darkgreen")

        # ======Search entry box======
        entry_search = Entry(self.window_portal, width=30, font=("Century Gothic", 10))
        entry_search.insert(END, '')
        entry_search.focus_set()
        entry_search.place(x=300, y=200)

        # ======Employee ID listbox======
        listbox_id = Listbox(self.window_portal, width=30, height=20, font=("Century Gothic", 10))
        listbox_id.place(x=300, y=250)

        # ======First name text======
        canvas.create_text(650, 450, text="First Name", font=("Century Gothic", 12, 'bold'), fill="darkgreen")

        # ======First name entry box======
        entry_first_name = Entry(self.window_portal, width=28, font=("Century Gothic", 10), state="disabled")
        entry_first_name.insert(END, '')
        entry_first_name.place(x=700, y=500)

        # ======Surname text======
        canvas.create_text(650, 500, text="Surname", font=("Century Gothic", 12, 'bold'), fill="darkgreen")

        # ======Surname entry box======
        entry_surname = Entry(self.window_portal, width=28, font=("Century Gothic", 10), state="disabled")
        entry_surname.insert(END, '')
        entry_surname.place(x=700, y=545)

        # ======Position text======
        canvas.create_text(650, 545, text="Position", font=("Century Gothic", 12, 'bold'), fill="darkgreen")

        # ======Position entry box======
        entry_position = Entry(self.window_portal, width=28, font=("Century Gothic", 10), state="disabled")
        entry_position.insert(END, '')
        entry_position.place(x=700, y=590)

        # ======Picture label======
        self.window_portal.default = PhotoImage(file="./images/user.png")

        label_picture = Label(self.window_portal, relief="raised", width=200, height=250,
                              image=self.window_portal.default)
        label_picture.place(x=700, y=200)

        # start methods
        search()
        live_clock()
