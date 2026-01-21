def CountDigit(No):
    icnt=0
    
    while(No!=0):
        i=No%10
        # print(i)
        icnt+=1
        No=No//10
    return icnt

def main():
    Value=int(input("Enter the number:"))
    Ret=CountDigit(Value)
    
    print("digit count is :",Ret)

if __name__=="__main__":
    main()