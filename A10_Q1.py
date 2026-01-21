def Table(No):
    for i in range(1,11):
        Table=No*i
        print(Table)

def main():
    Value=int(input("Enter the number:"))
    Table(Value)

if __name__=="__main__":
    main()