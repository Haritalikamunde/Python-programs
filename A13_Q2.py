import math

def Area(radius):
    Area=0
    Area=(radius**2)*(math.pi)
    return Area

def main():
    Value1=int(input("Enter length :"))
    Ret=Area(Value1)
    print("Area of rectangle is:", Ret)

if __name__=="__main__":
    main()