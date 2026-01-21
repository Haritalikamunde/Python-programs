def ChkGreater(No1, No2):
    if (No1>No2):
        print(No1," is greater")
    else:
        print(No2," is geater")

def main():
    Value1=int(input("Enter first number:"))
    Value2=int(input("Enter second number:"))

    Ret=ChkGreater(Value1, Value2)
    print("square root is:",Ret)

if __name__=="__main__":
    main()