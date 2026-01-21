def ChkPerfect(No):
    Sum=0
    temp=No
    for i in range(1,No):
        if(No%i==0):
            # print(i)
            Sum=Sum+i
    
    if (Sum==temp):
        return True
    else:
        return False

def main():
    Value=int(input("Enter the number:"))
    Ret=ChkPerfect(Value)
    if(Ret==True):
        print("Number is perfect")
    else:
        print("Number is not perfect")

if __name__=="__main__":
    main()