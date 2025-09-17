class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def display(self):
        print("name of stdent-",self.name," rollno-",self.rollno," marks-",self.marks)

s1=Student("bharath",1,(90,92,71))
s2=Student("Dham",2,(98,87,92))

s1.display()
s2.display()