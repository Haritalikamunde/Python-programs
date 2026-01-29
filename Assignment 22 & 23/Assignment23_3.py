class Numbers:

    def __init__(self,No):
        self.Value=No

    def ChkPrime(self):
        No_range=self.Value/2

        for i in range(2,int(No_range)):
            if(self.Value%i==0):
                return False
                break
        print("Number is prime")
        return True
    
    def ChkPrefect(self):

        if self.Value == self.SumFactors():
            print("Number is perfect")
            return True
        else:
            print("Number is not perfect")
            return False

    def Factors(self):
        
        for i in range(1,self.Value):
            if(self.Value % i==0):
                print(i)

    def SumFactors(self):
        Sum=0
        for i in range(1,self.Value):
            if(self.Value % i==0):
                Sum=Sum+i
                
        print("Sum of Factors is : ", Sum)
        return Sum

if __name__=="__main__":
    No=int(input("Enter the number: "))

    obj1=Numbers(No)
    obj1.ChkPrime()
    obj1.ChkPrefect()
    obj1.Factors()
    obj1.SumFactors()

  
