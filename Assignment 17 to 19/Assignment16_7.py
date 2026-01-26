def Isdivisible(No):
    
    if(No%5==0):
        return True
    else:
        return False

def main():
    Value=int(input("Enter the number:"))
    Ret=Isdivisible(Value)

    print(Ret)
    

if __name__=="__main__":
    main()