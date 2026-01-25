ChkSquare=lambda No:No**2

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    MData=list(map(ChkSquare,Data))
    print(MData)

if __name__=="__main__":
    main()