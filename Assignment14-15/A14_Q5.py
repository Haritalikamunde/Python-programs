CheckEven=lambda No:(No%2==0)

def main():
    Value=int(input("Enter the number:"))
    Ret=CheckEven(Value)
    print(Ret)
    
    if(Ret==True):
        print("Number is even")
    else:
        print("Number is odd")

if __name__=="__main__":
    main()
