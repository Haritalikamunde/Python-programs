def ChkPallindrome(No):
    icnt=0
    Temp=No
    rev=0
    while(No!=0):
        i=No%10
        rev=rev*10+i
        No=No//10
    print (rev)

    if(Temp==rev):
        return True
    else:
        return False

def main():
    Value=int(input("Enter the number:"))
    Ret=ChkPallindrome(Value)

    if(Ret==True):
        print("Pallindrome")
    else:
        print("Not Pallindrome")

if __name__=="__main__":
    main()