from functools import reduce

CheckGreat=lambda No:No>=70 and No<=90

Increment=lambda No:No+10

Add=lambda A,B:(A*B)

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)
    print("Actual Data is :",Data)

    FData=list(filter(CheckGreat,Data))

    print("Data after filter is :", FData)

    MData=list(map(Increment,FData))

    print("Data after map is :", MData)

    RData=reduce(Add,MData)

    print("Data after reduce is :", RData)

if __name__=="__main__":
    main()