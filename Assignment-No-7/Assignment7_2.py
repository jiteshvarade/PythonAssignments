
class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self,i):
        self.Radius = i

    def CalculateArea(self):
        self.Area = Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2*Circle.PI*self.Radius

    def Display(self):
        print("Area of circle is : ",self.Area)
        print("Circumference of circle is : ",self.Circumference)

if __name__ == "__main__":
    Obj1 = Circle()

    Obj1.Accept(5.6)
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()