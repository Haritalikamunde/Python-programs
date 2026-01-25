ChkOdd=lambda No:len(No)>5

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=input()
        Data.append(No)

    print(Data)

    FData=list(filter(ChkOdd,Data))
    print(FData)

if __name__=="__main__":
    main()