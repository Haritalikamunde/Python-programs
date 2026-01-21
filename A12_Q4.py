def PrintNumbers(No):
    
    for i in range(1,No+1):
        print(i)

def main():
    Value=int(input("Enter the number:"))
    PrintNumbers(Value)

if __name__=="__main__":
    main()