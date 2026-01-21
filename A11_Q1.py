def CheckPrime(No):
    
    No_range=No/2

    for i in range(2,int(No_range)):
        if(No%i==0):
            return False
            break
    return True

def main():
    Value=int(input("Enter the number:"))
    Ret=CheckPrime(Value)
    if(Ret==True):
        print("Number is prime")
    else:
        print("Number is not prime")

if __name__=="__main__":
    main()