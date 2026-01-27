import threading

def GetSum(Data):
    Sum=0
    for i in range(len(Data)):
        Sum=Sum+Data[i]
    print("Sum of elements is:",Sum)

def GetProduct(Data):
    Mult=1
    for i in range(len(Data)):
        Mult=Mult*Data[i]
    print("product of elements is :",Mult)
    

def main():
    Data=[]
    size=int(input("Enter the size of list :"))

    for i in range(size):
        No=int(input())
        Data.append(No)

    t1=threading.Thread(target=GetSum,args=(Data,))
    t1.start()

    t2=threading.Thread(target=GetProduct,args=(Data,))
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__=="__main__":
    main()