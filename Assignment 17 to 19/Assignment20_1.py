import threading

def DisplayEven():
    icnt=0
    No=1
    while icnt<10:
        if No%2==0:
            icnt+=1
            print(No)
        No+=1
    

def DisplayOdd():
    icnt=0
    No=1
    while icnt<10:
        if No%2!=0:
            icnt+=1
            print(No)
        No+=1

def main():

    t1=threading.Thread(target=DisplayEven)
    t1.start()

    t2=threading.Thread(target=DisplayOdd)
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__=="__main__":
    main()