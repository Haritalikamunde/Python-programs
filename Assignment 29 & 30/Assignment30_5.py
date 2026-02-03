import os
import sys

def CheckWordPresent(filename, findword):
    print(filename)
    Ret=os.path.exists(filename)

    if(Ret==False):
        print("There is no such file in directory")
        return

    fobj=open(filename,"r")
    Data=fobj.read()

    Words=Data.split()

    for i in Words:
        if i==findword:
            print("Word is present")

    fobj.close()

def main():
    
    if (len(sys.argv)!=3):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    CheckWordPresent(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()