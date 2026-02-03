import os
import sys

def DisplayLines(filename1):
    
    Ret=os.path.exists(filename1)

    if(Ret==False):
        print("There is no such file in directory")
        return

    fobj=open(filename1,"r")
    line=fobj.readline()

    while(line):
        print(line.strip())
        line=fobj.readline()

    fobj.close()

def main():
    
    if (len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    DisplayLines(sys.argv[1])

if __name__=="__main__":
    main()