# Command line input

import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border="-"*50

    Ret=False

    Ret=os.path.exists(FolderName)

    if Ret==True:
        Ret==os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable to create folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")
    
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    
    FileName=os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name :",FileName)

    fobj=open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Platform Surveillance System-----\n")
    fobj.write("Log created at: "+ time.ctime()+"\n")
    fobj.write(Border+"\n\n")
    fobj.write("-----------------System Report-------------------\n")

    # print("CPU Usage :", psutil.cpu_percent())
    fobj.write("CPU Usage :%s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")
    mem=psutil.virtual_memory()
    # print("RAM Usage :", mem.percent)
    fobj.write("RAM Usage :%s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage report\n")
    
    for part in psutil.disk_partitions():
        try:
            usage=psutil.disk_usage(part.mountpoint)
            # print(f'{part.mountpoint} used {usage.percent}%%')
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass
    fobj.write(Border+"\n")

    net=psutil.net_io_counters()
    fobj.write("\nNetwork Usage report\n")
    fobj.write(Border+"\n")

    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent/(1024*1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv/(1024*1024)))

    # Process Log

    data=ProcessScan()

    for info in data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("CPU_percent"))
        fobj.write("Memory : %s\n" %info.get("memory_percent"))
        fobj.write("Thread count :%s\n" %info.get("thread_count"))
        fobj.write("open files : %s\n" %info.get("open_files"))

        fobj.write(Border+"\n")
    

    fobj.write(Border+"\n")
    fobj.write("---------------- End of Log file -----------------\n")
    fobj.write(Border+"\n")
    fobj.close()

def ProcessScan():
    listProcess=[]

    # Warm up for CPU Percent

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    
    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["pid","name","username","status","create_time"])
            #convert create time
            try:
                info["create_time"]=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"]="NA"

            info["CPU_percent"]=proc.cpu_percent(None)
            info["memory_percent"]=proc.memory_percent()
            info["thread_count"]=proc.num_threads()
            try:
                files = proc.open_files()
                info["open_files"] = len(files) if files else 0
            except:
                info["open_files"]= "NA"
            
            listProcess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listProcess

def main():

    Border="-"*50
    print(Border)
    print("----- Marvellous Platform Surveillance System-----")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Send Mails with log")
            print("4 : Stor information about processes")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM Usage")
            print("7 : Store information about secondary storage")

        
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the Automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval: The time in minutes for periodic scheduling")
            print("DirectoryName: Name of directory to create auto logs ")

        else:
            print("Unable to proceed as there is no such option")
            print("please use --h or --u to get more details")

    # Python Demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time interval :",sys.argv[1])
        print("Directory name :",sys.argv[2])

        #Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started successfully")
        print("Directory created with name :",sys.argv[2])
        print("Time interval in minutes:",sys.argv[1])
        print("press Ctrl + C to stop the execution")

        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of arguments")
        print("Unable to proceed as there is no such option")
        print("please use --h or --u to get more details")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__=="__main__":
    main()