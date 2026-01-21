def MathsOperations(No1, No2):
    Addition=No1+No2
    print("Addition is:",Addition)

    Substraction=No1-No2
    print("Substraction is:",Substraction)

    Multiplication=No1*No2
    print("Multiplication is:",Multiplication)

    Division=No1/No2
    print("Division is:",Division)


def main():
    Value1=int(input("Enter the first number:"))
    Value2=int(input("Enter the second number:"))
    MathsOperations(Value1,Value2)

if __name__=="__main__":
    main()