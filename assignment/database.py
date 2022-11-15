import sqlite3

con = sqlite3.connect("../employees.db")
cur = con.cursor()

try:
    cur.execute(
        "CREATE TABLE Employee(emp_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(45), surname VARCHAR(45), "
        "gender VARCHAR(10), department VARCHAR(100), position VARCHAR(45), date_of_birth VARCHAR(10), start_date "
        "VARCHAR(10), email VARCHAR(60), contact VARCHAR(20), salary INTEGER(12), active BLOB, address VARCHAR(100), "
        "picture BLOB)")
    data = [
        (543, "Peter", "Parker", "Male", "IT", "Senior Software Engineer", "12/03/85", "05/11/16",
         "peterparker@gmail.com", "732-234-1248", 120000, True, "5432 Apple St,\nMaineville,\nWA 43171",
         "./images/peter.jpg"),
        (201, "Mary Jane", "Watson", "Female", "Accounting", "Tax Accountant", "24/07/89", "17/05/20",
         "mary_accounting@yahoo.co.uk", "874-345-8654", 76000, True, "8541 Summer Ave,\nPullman,\nNY 27811",
         "./images/mary.jpg")]

    cur.executemany("INSERT INTO Employee VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

except:
    print("Employee database has not been created as it already exists.")


