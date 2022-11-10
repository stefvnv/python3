import tkinter as tk
from PIL import ImageTk, Image
from os import listdir

size = 700, 700

window = tk.Tk()
window.title("Join")
window.geometry("700x700")
window.minsize(700, 700)
window.maxsize(700, 700)

bottomFrame = tk.Frame(window)
bottomFrame.pack(fill=tk.X, side=tk.BOTTOM)

for i in range(2):
    bottomFrame.columnconfigure(i, weight=1)


# commands
def one():
    global im, img, label
    print("one")
    # can't do this, or you'll overwrite the image!
    # im.save("one/"+ path)
    im = Image.open("one/" + path)

    im.thumbnail(size, Image.ANTIALIAS)

    img = ImageTk.PhotoImage(im)
    label.configure(image=img)


def two():
    global im, img, label
    print("two")
    # can't do this, or you'll overwrite the image!
    #    im.save("two/"+ path)
    im = Image.open("two/" + path)

    im.thumbnail(size, Image.ANTIALIAS)

    img = ImageTk.PhotoImage(im)
    label.configure(image=img)


# loop

imagesList = listdir("all/")

for path in imagesList:
    print("test")

    im = Image.open("all/" + path)

    im.thumbnail(size, Image.ANTIALIAS)

    img = ImageTk.PhotoImage(im)

    label = tk.Label(window, image=img)

    label.pack(side="top", fill="both", expand="true")

    bluebutton = tk.Button(bottomFrame, text="one", fg="blue", command=one)
    bluebutton1 = tk.Button(bottomFrame, text="two", fg="blue", command=two)

    bluebutton.grid(row=0, column=0, sticky=tk.W + tk.E)
    bluebutton1.grid(row=0, column=1, sticky=tk.W + tk.E)

    window.mainloop()
