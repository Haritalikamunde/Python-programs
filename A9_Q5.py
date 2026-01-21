
def Divisible(No):

    if (No%3==0) and (No%5==0):
        return True
    else:
        return False

def main():
    Value=int(input("Enter the number:"))
    Ret=Divisible(Value)

    if(Ret==True):
        print("divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
    

if __name__=="__main__":
    main()