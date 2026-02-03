import os
import sys

def CountfileLines(filename1):
    
    Ret=os.path.exists(filename1)

    if(Ret==False):
        print("There is no such file in directory")
        return

    fobj=open(filename1,"r")
    Data=fobj.readlines()
    print(len(Data))

    # icnt=0
    # for line in fobj:
    #     icnt=icnt+1
    # print(icnt)


    fobj.close()

def main():
    
    if (len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    CountfileLines(sys.argv[1])

if __name__=="__main__":
    main()