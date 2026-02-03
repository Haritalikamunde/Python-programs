import os
import sys

def CountWords(filename1):
    
    Ret=os.path.exists(filename1)

    if(Ret==False):
        print("There is no such file in directory")
        return

    fobj=open(filename1,"r")
    Data=fobj.read()

    Words=Data.split()
    print("Number of words are :",len(Words))

    fobj.close()

def main():
    
    if (len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    CountWords(sys.argv[1])

if __name__=="__main__":
    main()