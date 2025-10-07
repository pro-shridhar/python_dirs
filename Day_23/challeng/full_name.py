class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname.title() + " " + lastname.title()
        self.email = firstname.lower() + "." + lastname.lower() + "@company.com"


emp = Employee("Anurodh", "Bhosle")
print(emp.fullname)
print(emp.email)
