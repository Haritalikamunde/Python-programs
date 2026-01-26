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
        print("It is prime Number")
    else:
        print("It is not prime Number")

if __name__=="__main__":
    main()