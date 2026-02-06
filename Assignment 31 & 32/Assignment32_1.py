import hashlib
import os
import time
import sys

def CalculateCheckSum(FileName):
    
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DiectoryWatcher(DiectoryName="Demo"):

    Border="-"*50
    timestamp=time.ctime()

    LogFileName= "log%s.txt" %(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")
    fobj=open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file\n")
    fobj.write(Border+"\n")

    Ret=False

    Ret=os.path.exists(DiectoryName)

    if(Ret==False):
        print("There is No such Directory")
        return
    
    Ret=os.path.isdir(DiectoryName)

    if Ret==False:
        print("It is not a directory")
        return
    
    for FoldeName , SubFolderName, FileName in os.walk(DiectoryName):
        for FName in FileName:
            FName=os.path.join(FoldeName,FName)
            CheckSum= CalculateCheckSum(FName)
            fobj.write("File name: "+FName+"CheckSum : "+CheckSum+"\n")

    fobj.write("This log file is created at :"+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    if len(sys.argv)!=2:
        print("Enter correct number of arguments")
        return
    
    DiectoryWatcher(sys.argv[1])

    

if __name__=="__main__":
    main()