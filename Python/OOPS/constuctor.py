class Employee:
    company="LID"

    def __init__(self,salary,bond,name):
        self.salary=salary
        self.bond=bond
        self.name=name

    def get_salary(self):
        return self.salary
    # def bond(self):
    #     pass
    # def name(self):
    #     pass
    def get_info(self):
        print(f"The name of the Employee is {self.name}, salary is {self.salary},has bond for {self.bond}years")

e=Employee(34000,4,"Patrick")
print(e.get_salary())
(e.get_info())

