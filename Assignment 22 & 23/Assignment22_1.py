class Demo:
    Value=10

    def __init__(self,Value1,Value2):
        self.No1=Value1
        self.No2=Value2

    def fun(self):
        print("values of instance variables from fun are: ",self.No1,self.No2)

    def gun(self):
        print("values of instance variables from gun are: ",self.No1,self.No2)


if __name__=="__main__":
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()
