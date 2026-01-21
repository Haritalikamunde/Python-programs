
def Sqrt(No):
    Square=No**2
    return Square

def main():
    Value=int(input("Enter the number:"))
    Ret=Sqrt(Value)
    print("square root is:",Ret)

if __name__=="__main__":
    main()