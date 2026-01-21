def Cube(No1):
    cube=No1**3
    return cube

def main():
    Value=int(input("Enter the number:"))
    Ret=Cube(Value)
    print("Cube root is:",Ret)

if __name__=="__main__":
    main()