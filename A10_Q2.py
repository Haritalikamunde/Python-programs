def SumN(No):
    Sum=0
    for i in range(1,No+1):
        Sum=Sum+i
    return Sum

def main():
    Value=int(input("Enter the number:"))
    Ret=SumN(Value)
    print("Sum of natural numbers is:",Ret)

if __name__=="__main__":
    main()