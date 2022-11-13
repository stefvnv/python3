# TEST FILE - to be deleted

import sqlite3
from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Employee Portal | Employee Management System")
window.resizable(False, False)
from io import BytesIO
from PIL import Image, ImageTk

# testing

# Database
con = sqlite3.connect("../employees.db")
cur = con.cursor()

try:
    cur.execute(
        "CREATE TABLE Employee(emp_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(45), surname VARCHAR(45), "
        "gender VARCHAR(10), department VARCHAR(100), position VARCHAR(45), date_of_birth VARCHAR(10), start_date "
        "VARCHAR(10), email VARCHAR(60), contact VARCHAR(15), salary INTEGER(12), active BLOB, address VARCHAR(100), "
        "picture BLOB)")
    data = [
        (543, "Peter", "Parker", "Male", "IT", "Senior Software Engineer", "12/03/1985",
         "05/11/2016,peterparker@gmail.com", "0831239876", 120000, True, "5432 Apple St,\nMaineville,\nWA 43171",
         "peter.jpg"),
        (201, "Mary Jane", "Watson", "Female", "Accounting", "Tax Accountant", "24/07/1989", "17/05/2020",
         "peterparker@gmail.com", "0831239876", 120000, True, "8541 Summer Ave,\nPullman,\nNY 27811", "mary.jpg")]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

except:
    print("Employee Already Exists")


# MAKE THIS INTO ANOTHER CLASS
class Employee:
    def __init__(self, emp_id, first_name, surname, gender, department, position, date_of_birth, start_date, email,
                 contact, salary, active, address, picture):
        self.emp_id = emp_id
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.department = department
        self.position = position
        self.date_of_birth = date_of_birth
        self.start_date = start_date
        self.email = email
        self.contact = contact
        self.salary = salary
        self.active = active
        self.address = address
        self.picture = picture

    def read_id(self):
        return str(self.emp_id)

    def read_first_name(self):
        return self.first_name

    def read_surname(self):
        return self.surname

    def read_gender(self):
        return self.gender

    def read_department(self):
        return self.department

    def read_position(self):
        return self.position

    def read_dob(self):
        return self.date_of_birth

    def read_start_date(self):
        return self.start_date

    def read_email(self):
        return self.email

    def read_contact(self):
        return self.contact

    def read_salary(self):
        return self.salary

    def read_active(self):
        return self.active

    def read_address(self):
        return self.address

    def read_picture(self):
        # return self.picture
        return convert_to_binary_data(self.picture)


def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


cur.execute("select * from Employee")
double_array = cur.fetchall()

emp_list = []

for emp in double_array:
    emp_list.append(Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10],
                             emp[11], emp[12], emp[13]))

print(emp_list[0].read_picture())


img_byte = BytesIO(emp_list[0].read_picture())
# render_image = render_image.resize((250, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(Image.open(img_byte))


label_name = Label(window)

label_name.place(x=150, y=400)
label_name.config(image=image, borderwidth=4,  relief="solid")


mainloop()