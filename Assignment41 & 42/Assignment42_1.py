import math

def FindMean(List):
    Sum=0
    for i in List:
        Sum=i+Sum

    Mean=Sum/len(List)

    return Mean

def Find_bar(X, Mean):
    List=[]
    for i in X:
        El=i-Mean
        List.append(El)
    
    return List

def FindSum(Value):
    Sum=0
    for i in Value:
        Sum=Sum+i
    
    return Sum

def main():
    Border="-"*40
    print(Border)
    print("Manual Linear regression")
    X=[1, 2, 3, 4, 5]
    Y=[3, 4, 2, 4, 5]

    Mean_X=FindMean(X)
    Mean_Y=FindMean(Y)

    print(Border)

    print("Mean of X is : ",Mean_X)
    print("Mean of Y is : ",Mean_Y)

    print(Border)

    X_bar=Find_bar(X, Mean_X)
    Y_bar=Find_bar(Y, Mean_Y)

    XY_barSum=[]
    for i in range(len(X_bar)):
        Mult=X_bar[i]*Y_bar[i]
        XY_barSum.append(Mult)
    
    # print(XY_barSum)
    
    Summation_XY_Bar=FindSum(XY_barSum)
    
    # print(Summation_XY_Bar)
    S=0
    Sum_bar=0
    for i in range(len(X_bar)):
        S=X_bar[i]**2
        Sum_bar=Sum_bar+S

    Slope=Summation_XY_Bar/Sum_bar
    print("Slope (m) is : ",Slope)

    print(Border)

    Intercept=Mean_Y-(Slope*Mean_X)
    print("Intercept (c) is :",Intercept)

    print(Border)
    print("Regression_Eq is : Y=0.4X+2.4")

    print(Border)
    x=6
    predicted_Y=(Slope*x)+Intercept
    print("predicted Y for X=6 :",predicted_Y)

    print(Border)

if __name__=="__main__":
    main()
