def DisplayEven():
    icnt=0
    No=1
    while icnt<10:
        if No%2==0:
            icnt+=1
            print(No)
        No+=1

def main():
    DisplayEven()
    

if __name__=="__main__":
    main()