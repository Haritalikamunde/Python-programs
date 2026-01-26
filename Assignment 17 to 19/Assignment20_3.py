import threading

def EvenList(Data):
    sum=0
    for i in range(len(Data)):
        if Data[i]%2==0:
            sum=sum+Data[i]
    print(sum)

def OddList(Data):
    sum=0
    for i in range(len(Data)):
        if Data[i]%2!=0:
            sum=sum+Data[i]
    print(sum)

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    print(Data)

    t1=threading.Thread(target=EvenList,args=(Data,))
    t1.start()

    t2=threading.Thread(target=OddList,args=(Data,))
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__=="__main__":
    main()