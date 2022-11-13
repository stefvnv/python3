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
        return convert_to_binary_data(self.picture)


def convert_to_binary_data(filename):
    """Converts digital data to binary format"""

    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data
