def MinNum(Data, Num):
    icnt=0
    for i in range(len(Data)):
        if (Data[i]==Num):
            icnt+=1
    return icnt

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    # print(Data)
    No=int(input("Enter the number to find frequency :"))

    ret=MinNum(Data,No)

    print("frequency of number is:",ret)
    print(ret)

if __name__=="__main__":
    main()