def ChkNum(No):
    
    if(No>0):
        print("Positive Number")
    elif(No==0):
        print("Zero")
    else:
        print("Negative Number")

def main():
    Value=int(input("Enter the number:"))
    ChkNum(Value)

if __name__=="__main__":
    main()