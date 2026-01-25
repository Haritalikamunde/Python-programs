from functools import reduce

Min=lambda A,B:min(A,B)

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    RData=reduce(Min,Data)
    print(RData)

if __name__=="__main__":
    main()