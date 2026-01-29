class Arithmetic:
    PI=3.14

    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self,No1,No2):
        self.value1=No1
        self.value2=No2

    def Addition(self):
        Addition=self.value1+self.value2
        print("Addition is: ",Addition)

    def Substraction(self):
        Addition=self.value1-self.value2
        print("Substraction is: ",Addition)

    def Multiplication(self):
        Addition=self.value1*self.value2
        print("Multiplication is: ",Addition)

    def Division(self):
        Addition=self.value1/self.value2
        print("Division is: ",Addition)

if __name__=="__main__":
    obj1=Arithmetic()
    obj1.Accept(21,11)
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()

    obj2=Arithmetic()
    obj2.Accept(51,11)
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()