import threading

def PrintSmallChar(Data):
    print("Small thread ID is:", threading.get_ident())
    for i in Data:
        if i>="a" and i<="z":
            print("Print Small Character is:",i)

def PrintCapitalChar(Data):
    print("Capital thread ID is:", threading.get_ident())
    for i in Data:
        if i>="A" and i<="Z":
            print("Print Capital Character is:",i)

def PrintNumChar(Data):
    print("Digits thread ID is:", threading.get_ident())
    for i in Data:
        if i.isdigit():
            print("Print digit is :",i)

def main():
    Data=input("Enter the String :")

    t1=threading.Thread(target=PrintSmallChar,args=(Data,))
    t1.start()

    t2=threading.Thread(target=PrintCapitalChar,args=(Data,))
    t2.start()

    t3=threading.Thread(target=PrintNumChar,args=(Data,))
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("end of main")

if __name__=="__main__":
    main()