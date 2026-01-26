def MaxNum(Data):
    Max=Data[0]
    for i in range(len(Data)):
        if (Data[i]>Max):
            Max=Data[i]
    return Max

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    ret=MaxNum(Data)

    print("Maximum number is:",ret)
    print(ret)

if __name__=="__main__":
    main()