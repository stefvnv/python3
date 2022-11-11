from tkinter import *
from tkinter import messagebox
from portal import *

window = Tk()
window.geometry("1280x720")
window.title("Employee Portal - Employee Management System | Login")
window.resizable(False, False)


def show_password():
    """Shows or hides password based on whether checkbutton is selected"""

    p = password.get()

    if var_checkbutton.get() == 1:
        entry_password.config(show="")
        entry_password.delete(0, END)
        entry_password.insert(END, p)
    else:
        entry_password.config(show="•")
        entry_password.delete(0, END)
        entry_password.insert(END, p)


def login():
    """Logs user in if username and password entries are correct"""

    if entry_username.get() == "root" and password.get() == "pw":
        initiate_portal(window)

        # removes login window
        window.withdraw()
        messagebox.showinfo("Success", "You have logged in to Employee Portal successfully.")
    else:
        messagebox.showerror("Error", "The login information entered is incorrect.\nTry again.")


frame = Frame(window, width=800, height=500, bg="green", borderwidth=2, relief="solid")
frame.place(x=250, y=100)

# ======Title======
label_title = Label(window, text="Login", fg="blue", bg="yellow", font=("arial", 16, "bold"))
label_title.place(x=600, y=80)

# ======Username label======
label_username = Label(window, text="Username", fg="blue", bg="white", font=("arial", 16, "bold"))
label_username.place(x=400, y=200)

# ======Username entry box======
entry_username = Entry(window, width=20)
entry_username.insert(END, '')
entry_username.place(x=600, y=200)

# ======Password label======
label_password = Label(window, text="Password", fg="blue", width=15, font=("arial", 10, "bold"))
label_password.place(x=400, y=300)

# ======Password entry box======
password = StringVar()

entry_password = Entry(window, width=20, textvariable=password, show="•")
entry_password.insert(END, '')
entry_password.place(x=600, y=300)

# ======Forgot password checkbox======
var_checkbutton = IntVar()
checkbutton_show_password = Checkbutton(window, text="Show password", variable=var_checkbutton, command=show_password)
checkbutton_show_password.place(x=600, y=400)

# ======Login button======
button_login = Button(window, text="Login", fg="black", font=("arial", 10, "bold"), command=login)
button_login.place(x=600, y=500)

mainloop()
