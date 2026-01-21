def binary(No):
    if No == 0:
        print(0)
        return

    binary = ""

    while (No!= 0):
        icnt = No % 2
        binary = str(icnt) + binary
        No = No // 2

    print(binary)

def main():
    Value = int(input("Enter the number: "))
    binary(Value)


if __name__ == "__main__":
    main()
