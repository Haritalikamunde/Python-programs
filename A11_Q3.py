def SumDigit(No):
    icnt=0
    Sum=0
    while(No!=0):
        i=No%10
        # print(i)
        Sum=Sum+i
        No=No//10
    return Sum

def main():
    Value=int(input("Enter the number:"))
    Ret=SumDigit(Value)
    
    print("digit count is :",Ret)

if __name__=="__main__":
    main()