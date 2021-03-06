class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = "Reyhan"
# emp_1.last = "Alemmario"
# emp_1.email = "reyhanalemmario1@gmail.com"
# emp_1.pay = 840

# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "Test.User@company.com"
# emp_2.pay = 300

# print(emp_1.email)
# print(emp_2.email)


emp_1 = Employee("Reyhan", "Alemmario", "840")
emp_2 = Employee("Test", "User", "300")

# print(emp_1.email)
# print(emp_2.email)

# The same thing
print(emp_1.fullname())
print(Employee.fullname(emp_1))
