class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self,Value):
        self.Radius=Value

    def CalculateArea(self):
        self.Area=Circle.PI*(self.Radius**2)
        print("Area is :",self.Area)

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
        print("Circumference is :",self.Circumference)


if __name__=="__main__":
    obj1=Circle()
    obj1.Accept(11)
    obj1.CalculateArea()
    obj1.CalculateCircumference()

    obj2=Circle()
    obj2.Accept(21)
    obj2.CalculateArea()
    obj2.CalculateCircumference()