import threading

def MaxNum(Data):
    Max=Data[0]
    for i in range(len(Data)):
        if (Data[i]>Max):
            Max=Data[i]
    print("Maximum number is:",Max)

def MinNum(Data):
    Min=Data[0]
    for i in range(len(Data)):
        if (Data[i]<Min):
            Min=Data[i]
    print("Minimum number is :",Min)
    

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    t1=threading.Thread(target=MaxNum,args=(Data,))
    t1.start()

    t2=threading.Thread(target=MinNum,args=(Data,))
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__=="__main__":
    main()