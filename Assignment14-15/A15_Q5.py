from functools import reduce

Max=lambda A,B:max(A,B)

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    RData=reduce(Max,Data)
    print(RData)

if __name__=="__main__":
    main()