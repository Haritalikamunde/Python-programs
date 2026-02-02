import os

def CheckFileExist(filename):

    Ret=os.path.exists(filename)
    
    if(Ret==True):
        print("file is present in the given directory")
    else:
        print("There is no such file in directory")


def main():
    FileName=input("Enter the file name:")

    CheckFileExist(FileName)

if __name__=="__main__":
    main()