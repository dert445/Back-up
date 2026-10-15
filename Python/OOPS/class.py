class Employee:
    company="LID"

    def get_salary(self):
        return 20000


a=Employee()
print(a.get_salary())

a2=Employee()
print(a2.get_salary())

print(a2.company)