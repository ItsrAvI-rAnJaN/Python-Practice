class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return 3.1459 * self.radius ** 2
    
    def getPerimeter(self):
        return 2 * 3.1459 * self.radius




if __name__== "__main__":
    circy = Circle(11)
    print(circy.getArea())
    # circy = Circle(4.44)
    # print( circy.getPerimeter())
