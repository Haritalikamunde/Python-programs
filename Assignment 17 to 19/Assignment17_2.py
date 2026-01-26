
def Display(row,col):
    
    for i in range(row):
        for j in range(col):
            print("*",end=" ")
        print()

def main():
    No1=0
    No2=0

    No1=int(input("Enter first number :"))
    No2=int(input("Enter second number :"))

    Display(No1,No2)

if __name__=="__main__":
    main()