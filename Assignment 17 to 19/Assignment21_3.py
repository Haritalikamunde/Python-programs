import threading

iCnt=1
lobj= threading.Lock()

def Update():
    global iCnt
    
    for i in range(1,1000000):
        with lobj:
            iCnt= iCnt+2


def main():
    global iCnt
    
    t1=threading.Thread(target=Update)
    t2=threading.Thread(target=Update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt is :",iCnt)

if __name__=="__main__":
    main()