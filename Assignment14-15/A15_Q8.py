ChkOdd=lambda No:No%3==0 and No%5==0

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    FData=list(filter(ChkOdd,Data))
    print(FData)

if __name__=="__main__":
    main()