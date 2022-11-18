from portal import *
from fonts import *

window = Tk()
window.geometry("1280x720")
window.title("Employee Portal - Employee Management System | Login")
window.resizable(False, False)

background = PhotoImage(file="./images/background.png")


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

    # if entry_username.get() == "root" and password.get() == "pw":
    initiate_portal(window)

    # removes login window
    window.withdraw()
    messagebox.showinfo("Success", "You have successfully logged in to Employee Portal.")
    # else:
    #     messagebox.showerror("Error", "The login information entered is incorrect.\nTry again.")


# ====== Canvas ======
canvas = Canvas(window, width=1280, height=720, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ====== Background image ======
canvas.create_image(0, 0, image=background, anchor="nw")

# ======Title text======
canvas.create_text(640, 80, text="Employee Portal", font=title_font, fill="white")
canvas.create_text(640, 200, text="Login", font=header_font, fill="lightgreen")

# ======Username text======
canvas.create_text(550, 300, text="Username", font=body_font, fill="white")

# ======Username entry box======
entry_username = Entry(window, width=20)
entry_username.insert(END, '')
entry_username.focus_set()
entry_username.place(x=600, y=300)

# ======Password text======
canvas.create_text(550, 380, text="Password", font=body_font, fill="white")

# ======Password entry box======
password = StringVar()

entry_password = Entry(window, width=20, textvariable=password, show="•")
entry_password.insert(END, '')
entry_password.place(x=600, y=380)

# ======Forgot password checkbox======
var_checkbutton = IntVar()
checkbutton_show_password = Checkbutton(window, text="Show password", variable=var_checkbutton, command=show_password)
checkbutton_show_password.place(x=600, y=430)

# ======Login button======
button_login = Button(window, text="Login", fg="black", font=("arial", 10, "bold"), command=login)
button_login.place(x=620, y=500)

mainloop()
