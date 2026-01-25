CheckDivisible=lambda No:(No%5==0)

def main():
    Value=int(input("Enter the number:"))
    Ret=CheckDivisible(Value)
    print(Ret)

if __name__=="__main__":
    main()
