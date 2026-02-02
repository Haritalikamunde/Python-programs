import os

def DisplayFileData(filename):

    Ret=os.path.exists(filename)
    
    if(Ret==True):
        f=open(filename,"r")
        print(f.read(10))
    else:
        print("There is no such file in directory")


def main():
    FileName=input("Enter the file name:")

    DisplayFileData(FileName)

if __name__=="__main__":
    main()