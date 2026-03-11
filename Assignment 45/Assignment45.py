import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousClassifier(DataPath):
    border="-"*40

    # Step 1: Get Data
    print(border)
    print("Step 1: Load the dataset from csv file")
    print(border)

    df=pd.read_csv(DataPath)
    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

    # Step 2: clean prepare and manipulate the data
    print(border)
    print("Step 2: clean prepare and manipulate the data")
    print(border)

    df.dropna(inplace=True)
    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])
    print(border)

    # Separate independent and dependent variables
    print(border)
    print("Separate independent and dependent variables")
    print(border)

    X=df.drop(columns=['Class'])
    Y=df['Class']
    
    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    # Split the dataset for training and testing

    print(border)
    print("split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train Shape : ", X_train.shape)
    print("X_test Shape : ", X_test.shape)
    print("Y_train Shape : ", Y_train.shape)
    print("Y_test Shape : ", X_test.shape)
    
    #--------------------------------------------------------
    # Step 3 : Train the model
    #--------------------------------------------------------

    print(border)
    print("Step 3 : Train the model")
    print(border)

    model=LinearRegression()
    model.fit(X_train, Y_train)

    #--------------------------------------------------------
    # Step 4 : Test the Data
    #--------------------------------------------------------

    print(border)
    print("Step 4 : Test the Data")
    print(border)

    Y_pred=model.predict(X_test)

    MSE=mean_squared_error(Y_test, Y_pred)
    RMSE=np.sqrt(MSE)

    R2=r2_score(Y_test, Y_pred)

    print("Mean Square error : ", MSE)
    print("Root mean square error : ", RMSE)
    print("R square value : ", R2*100)


def main():
    border="-"*40
    print(border)
    print("Wine classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()