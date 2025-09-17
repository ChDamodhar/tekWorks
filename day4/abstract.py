from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b 
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 2*3.14*self.r

rec=Rectangle(5,7)
cir=Circle(6)
print("Rectangle area:",rec.area())
print("Circle Area:",cir.area())
