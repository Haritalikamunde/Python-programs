import threading

def DisplayEven(No):
    No_range=No/2

    for i in range(2,int(No_range)):
        if(No%i==0):
            print(i)
    

def DisplayOdd(No):
    No_range=No/2

    for i in range(2,int(No_range)):
        if(No%i!=0):
            print(i)

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    t1=threading.Thread(target=DisplayEven,args=(Data,))
    t1.start()

    t2=threading.Thread(target=DisplayOdd,args=(Data,))
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__=="__main__":
    main()