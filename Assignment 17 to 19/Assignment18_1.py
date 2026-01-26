def SumList(Data):
    sum=0
    for i in range(len(Data)):
        sum=sum+Data[i]
    return sum

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    ret=SumList(Data)

    print("Sum of numbers is :",ret)
    print(ret)

if __name__=="__main__":
    main()