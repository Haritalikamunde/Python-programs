def ReverseDigit(No):
    icnt=0
    rev=0
    while(int(No)!=0):
        i=No%10
        rev=rev*10+i
        No=No//10
    print (rev)

def main():
    Value=int(input("Enter the number:"))
    ReverseDigit(Value)

if __name__=="__main__":
    main()