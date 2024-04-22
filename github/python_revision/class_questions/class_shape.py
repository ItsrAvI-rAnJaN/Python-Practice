# pseduo Code
"""
class Shape(ABC):
    area()
        abstract method
class circle(Shape):
    area(radius)
        return 3.14*radius*radius
class Rectangle(shape):
    area(length,breadth):
        return :Length*breath
class Triangle(Shape):
    area(base,height)
      return: 0.5*base*height
    
"""



from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

class Triangle(Shape):
    def __init__(self,l,h):
        self.l=l
        self.h=h
    def area(self):
        return 0.5*self.l*self.h









if __name__=='__main__':
    # obj=Circle(2)
    # obj=Rectangle(12,2)
    # obj=Triangle(12,2)
    print( obj.area())

