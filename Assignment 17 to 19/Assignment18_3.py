def MinNum(Data):
    Min=Data[0]
    for i in range(len(Data)):
        if (Data[i]<Min):
            Min=Data[i]
    return Min

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    ret=MinNum(Data)

    print("Minimum number is:",ret)
    print(ret)

if __name__=="__main__":
    main()