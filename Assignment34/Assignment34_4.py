import time
import os
import shutil
import hashlib
import sys
import schedule
import zipfile
from pathlib import Path

def makeLogFile(files,zip_file,Stime):
    Border="-"*50
    LogFolder="LogFiles"

    if not os.path.exists(LogFolder):
        os.mkdir(LogFolder)
    
    timestamp=time.strftime("%Y-%m-%d_%H_%M_%S")
    
    FileName=os.path.join(LogFolder,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name :",FileName)

    fobj=open(FileName,'w')

    fobj.write("-------------------Backup Logs----------------------\n")
    fobj.write("Backup Completed sucessfully \n")
    fobj.write("Backup started at :" +str(Stime)+"\n")
    fobj.write("files copied: "+ str(len(files))+"\n")
    fobj.write("created zip file is : "+ zip_file+"\n")
    fobj.write(Border+"\n")

def Extract_zip(source, destination):

    source_absPath=os.path.abspath(source)
    dest_abspath=os.path.abspath(destination)

    fobj=zipfile.ZipFile(source_absPath, 'r')

    fobj.extractall(dest_abspath)

    print("files extracted sucess")    


def make_zip(folder):
    timeStamp=time.strftime("%Y-%m-%d_%H_%M_%S")

    Zip_name=folder+"_"+timeStamp+".zip"

    zobj=zipfile.ZipFile(Zip_name,'w',zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path=os.path.join(root,file)
            relative=os.path.relpath(full_path,folder)
            zobj.write(full_path,relative)

    zobj.close()

    return Zip_name


def calculate_hash(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    while True:
        data=fobj.read(1024)

        if not data:
            break
        else:
            hobj.update(data)
        
    fobj.close()

    return hobj.hexdigest()



def BackupFiles(source, destination):
    copied_files=[]

    if (os.path.isdir(source))==False:
        print("directory to be backedup is not present")

    os.makedirs(destination,exist_ok=True)
    
    startTime=time.strftime("%Y-%m-%d_%H_%M_%S")
    
    for root , dir, files in os.walk(source):
        for file in files:
            src_path=os.path.join(root,file)

            if Path(src_path).suffix == ".txt":
                continue

            rel_path=os.path.relpath(src_path,source)
            dest_path=os.path.join(destination,rel_path)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            if((not os.path.exists(dest_path))or (calculate_hash(src_path)!=calculate_hash(dest_path))):
                shutil.copy2(src_path,dest_path)
                copied_files.append(rel_path)

    return copied_files, startTime



def DataShield(Source="Data"):
    Border="-"*50

    BackupFolderName="BackupFiles"

    print(Border)
    print("Backup process time is: ",time.ctime())
    print("Border")

    files, Stime=BackupFiles(Source, BackupFolderName)

    zip_file=make_zip(BackupFolderName)

    makeLogFile(files,zip_file, Stime)

    print(Border)
    print("Backup Completed sucessfully")
    print("files copied: ", len(files))
    print("zip file gets created: ", zip_file)
    print(Border)



def main():

    Border="-"*50
    print(Border)
    print("-----------Data Shield System------------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to")
            print("1 : Takes Auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the Automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic scheduling")
            print("SourceDirectory: Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("please use --h or --u to get more details")

    # Python Demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time interval :",sys.argv[1])
        print("Directory name :",sys.argv[2])

        #Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(DataShield, sys.argv[2])

        print(Border)
        print("Data Sheild System started successfully")
        print("Time interval in minutes:",sys.argv[1])
        print("press Ctrl + C to stop the execution")
        print(Border)

        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv)==4):
        Extract_zip(sys.argv[2],sys.argv[3])

    else:
        print("Invalid Number of arguments")
        print("Unable to proceed as there is no such option")
        print("please use --h or --u to get more details")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__=="__main__":
    main()