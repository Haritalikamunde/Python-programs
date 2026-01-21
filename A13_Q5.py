def Result(Marks):
    if(Marks>=100):
        print("marks are not valid")
    elif(Marks>=75):
        print("Distinction")
    elif(Marks>=60):
        print("first class")
    elif(Marks>=50):
        print("Second class")
    else:
        print("Fail")


def main():
    Value=int(input("Enter the number:"))
    Result(Value)
    

if __name__=="__main__":
    main()