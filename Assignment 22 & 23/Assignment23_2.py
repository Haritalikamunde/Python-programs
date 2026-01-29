class BankAccount:
    ROI=10.5

    def __init__(self,ACName, ACBalance):
        self.Name=ACName
        self.Amount=ACBalance

    def Display(self):
        print(f"Account holder name is :{self.Name}\nAccount balance is :{self.Amount} ")

    def Deposite(self, Deposite):
        self.Amount=self.Amount+Deposite

        print("Account balance after Deposite is:",self.Amount)

    def Withdraw(self, Withdraw_ammount):
        if self.Amount>Withdraw_ammount :
            self.Amount=self.Amount-Withdraw_ammount
            print("Account balance after withdrawal is:",self.Amount)
        else:
            print("Insufficient balance to withdraw")


    def CalculateInterest(self):
        Interest=(self.Amount*BankAccount.ROI)/100

        print("Interest is:",Interest)


if __name__=="__main__": 
    obj1=BankAccount("Radha",1000)
    obj1.Display()
    obj1.Deposite(500)
    obj1.Withdraw(200)
    obj1.CalculateInterest()

    print("-"*50)
    obj2=BankAccount("Ram",500)
    obj2.Display()
    obj2.Deposite(100)
    obj2.Withdraw(900)
    obj2.CalculateInterest()
