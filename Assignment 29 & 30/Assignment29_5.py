import os
import sys

def FindFrequency(filename, findword):
    print(filename)
    Ret=os.path.exists(filename)

    if(Ret==False):
        print("There is no such file in directory")
        return

    fobj=open(filename,"r")
    Data=fobj.read()

    Words=Data.split()
    icnt=0
    for i in Words:
        if i==findword:
            icnt=icnt+1
    
    print(f'Word is persent {icnt} times')
            
    fobj.close()

def main():
    
    if (len(sys.argv)!=3):
        print("Invalid number of arguments")
        print("please enter filename ")
        return
    
    FindFrequency(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()