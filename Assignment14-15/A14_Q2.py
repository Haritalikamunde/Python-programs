CheckCube=lambda No:(No**3)

def main():
    Value=int(input("Enter the number:"))
    Ret=CheckCube(Value)
    print("Cube is ",Ret)

if __name__=="__main__":
    main()
