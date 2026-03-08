import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def PredictSalary():
    
    X=[1,2,3,4,5]
    Y=[20000,25000,30000,35000,40000]

    print("Values of independent variables : X -",X)
    print("Values of dependent variables :Y- ", Y)

    mean_x=np.mean(X)                     
    mean_Y=np.mean(Y)                     

    print("X_mean is :", mean_x)
    print("Y_mean is :", mean_Y)

    n=len(X)       

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator=numerator +((X[i]-mean_x) *(Y[i]-mean_Y))
        denominator=denominator +((X[i]-mean_x)**2)

    m= numerator/ denominator

    print("Slope of line i.e. m:", m)

    c=mean_Y-(m*mean_x)

    print("Y intercept of line ie. c :",c)
    
    x=np.linspace(1,6,n)
    y=c+m*x

    # for prediction of 6 years of experience salary 

    Yp=m*6+c
    print("Salary for 6 years experience is :",Yp)

def main():
    PredictSalary()


if __name__=="__main__":
    main()



