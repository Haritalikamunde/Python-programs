import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            Sum += i
            print("Even factor Sum is :", Sum)

def OddFactor(No):
    Sum = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            Sum += i
            print("Odd factor Sum is :", Sum)

def main():
    Value=int(input("Enter the number :"))

    t1=threading.Thread(target=EvenFactor,args=(Value,))
    t1.start()

    t2=threading.Thread(target=OddFactor,args=(Value,))
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__=="__main__":
    main()