class Emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("name of employee-",self.name," salary-",self.salary)

class Manager(Emp):
    def __init__(self,name,salary,depart):
        super().__init__(name,salary)
        self.depart = depart
    def display(self):
        super().display()
        print("department-",self.depart)

e1=Emp("Bharath",50000)
m1=Manager("Damodhar",90000,"developer")

e1.display()
m1.display()