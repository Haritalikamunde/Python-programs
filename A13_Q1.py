def Area(length, width):
    Area=0
    Area=length*width
    return Area

def main():
    Value1=int(input("Enter length :"))
    Value2=int(input("Enter width :"))
    Ret=Area(Value1,Value2)
    print("Area of rectangle is:", Ret)

if __name__=="__main__":
    main()