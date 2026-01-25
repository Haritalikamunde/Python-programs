CheckMax=lambda No1 ,No2:(No1>No2)

def main():
    Value1=int(input("Enter first number:"))
    Value2=int(input("Enter second number:"))
    Ret=CheckMax(Value1, Value2)
    
    if(Ret==True):
        print("No 1 is Maximum")
    else:
        print("No 2 is Maximum")

if __name__=="__main__":
    main()
