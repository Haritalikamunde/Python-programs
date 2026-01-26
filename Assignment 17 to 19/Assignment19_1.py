ChkSquare=lambda No:No**2

def main():
    Value=int(input("Enter the Number :"))

    ret=ChkSquare(Value)
    print(ret)

if __name__=="__main__":
    main()