import sys
import os
from pathlib import Path
import shutil
import time

def DirectoryFileSearch(filename,TempFolder):
    Border="-"*50
    timestamp=time.ctime()

    LogFileName= "log%s.log" %(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")
    fobj=open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file\n")
    fobj.write(Border+"\n")

    Ret=os.path.exists(filename)

    if(Ret==False):
        print("there is no such directory named as :", filename)
        return

    Ret=os.path.isdir(filename)

    if (Ret==False):
        print("This is not a directory")

    for FolderName, SubFolderName, FileName in os.walk(filename):
        shutil.copytree(FolderName,TempFolder)

    fobj.write("files copied successfully into new directory\n")
    fobj.write("This log file is created at :"+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    if len(sys.argv)!=3:
        print("Enter correct number of arguments")
        return
    
    DirectoryFileSearch(sys.argv[1],sys.argv[2])


if __name__=="__main__":
    main()