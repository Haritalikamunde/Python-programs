import os
import sys

def CompareData(filename1, filename2):
    
    Ret=os.path.exists(filename1)

    if(Ret==False):
        print("There is no such file in directory")
        return

    f1=open(filename1,"r")
    Data1=f1.read()
    
    f2=open(filename2,"r")
    Data2=f2.read()

    if(Data1==Data2):
        print("Success")
    else:
        print("Failure")

    f1.close()
    f2.close()

def main():
    
    if (len(sys.argv)!=3):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    CompareData(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()