ChkEven=lambda No:No%2==0

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    FData=list(filter(ChkEven,Data))
    print(FData)

if __name__=="__main__":
    main()