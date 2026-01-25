CheckEven=lambda No:(No%2!=0)

def main():
    Value=int(input("Enter the number:"))
    Ret=CheckEven(Value)
    print(Ret)

if __name__=="__main__":
    main()
