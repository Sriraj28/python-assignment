class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

    def details(self):
        print(self.name, self.emp_id, self.dept)

m = Manager("Yatharth", "E101", "IT")
m.details()