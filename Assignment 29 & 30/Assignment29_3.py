import os
import sys

def CopyFileData(filename):
    print(filename)
    Ret=os.path.exists(filename)

    if(Ret==False):
        print("There is no such file in directory")
        return

    f=open(filename,"r")
    Data=f.read()
    
    W=open("Demo.txt","a")
    W.write(Data)

    W.close()
    f.close()

def main():
    
    if (len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    CopyFileData(sys.argv[1])

if __name__=="__main__":
    main()