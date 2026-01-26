def PrintEven(No):
    
    if(No%2==0):
        return True

def main():
    Value=int(input("Enter the number:"))
    Ret=PrintEven(Value)

    if(Ret==True):
        print("Even number")
    else:
        print("odd number")
    

if __name__=="__main__":
    main()