class Employee:
    company="LID"

    def __init__(self,salary,bond,name,company):
        self.salary=salary
        self.bond=bond
        self.name=name
        self.company=company

    def get_salary(self):
        return self.salary
    # def bond(self):
    #     pas
    # def name(self):
    #     pass
    def get_info(self):
        print(f"The name of the Employee is {self.name}, salary is {self.salary},has bond for {self.bond}years")

e1=Employee(80000,20,"Dert","GOI")
print(e1.company)
print(Employee.company)
