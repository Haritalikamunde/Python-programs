import os
import sys

def CopyFileData(filename1,filename2):
    print(filename1)
    Ret=os.path.exists(filename1)

    if(Ret==False):
        print("There is no such file in directory")
        return

    f=open(filename1,"r")
    Data=f.read()
    
    W=open(filename2,"a")
    W.write(Data)

    W.close()
    f.close()

def main():
    
    if (len(sys.argv)!=3):
        print("Invalid number of arguments")
        print("please enter filename1 ")
        return
    
    CopyFileData(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()