from functools import reduce

CheckEven=lambda No:(No%2==0)

Increment=lambda No:No*2

Add=lambda A,B:max(A,B)

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)
    print("Actual Data is :",Data)

    FData=list(filter(CheckEven,Data))

    print("Data after filter is :", FData)

    MData=list(map(Increment,FData))

    print("Data after map is :", MData)

    RData=reduce(Add,MData)

    print("Data after reduce is :", RData)

if __name__=="__main__":
    main()