import Assignment17_1 as imp

def main():
    Value1=0
    Value2=0
    result=0

    Value1=int(input("Enter first number :"))
    Value2=int(input("Enter second number :"))

    Result=0
    Result=imp.Add(Value1,Value2)
    print("Addition is :",Result)

    Result=imp.Sub(Value1,Value2)
    print("Substraction is :",Result)

    Result=imp.Mul(Value1,Value2)
    print("Multiplication is :",Result)

    Result=imp.Div(Value1,Value2)
    print("Division is :",Result)

if __name__=="__main__":
    main()