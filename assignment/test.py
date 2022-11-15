# TEST FILE - to be deleted
from tkinter import *


class NewWindow:
    instance = None

    @staticmethod
    def open_instance():
        if NewWindow.instance is None:
            window_new = Toplevel(window)
            window_new.geometry("200x100")
            NewWindow()

    def __init__(self):
        if NewWindow.instance is None:
            NewWindow.instance = self


window = Tk()
window.geometry("800x600")
window.title("Test")
window.resizable(False, False)


button = Button(window, text="Open Instance", command=NewWindow.open_instance)
button.place(x=620, y=500)

mainloop()
