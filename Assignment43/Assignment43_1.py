import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
from sklearn.preprocessing import LabelEncoder

def Predictor(DataPath):
    df=pd.read_csv(DataPath)

    print("Few records from the dataset.:")
    print(df.head())
  
    print("Removing Unwanted columns")

    print(df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace= True)

    print("dataset after removing empty values :")
    print(df.shape)

    print(df.head())

    print("Check missing values ")

    print("Missing values are ")
    print(df.isnull().sum())


    print("statistical summary of dataset")
    print(df.describe())
    
    le=LabelEncoder()

    df['Whether']=le.fit_transform(df["Whether"])
    df['Temperature']=le.fit_transform(df["Temperature"])

    Features=["Whether","Temperature"]
    
    X = df.drop('Play', axis=1)
    Y = df['Play']

    print("Shape if independent variables : ", X.shape)
    print("Shape of dependent variable : ",Y.shape)


    X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.2,random_state=42)
    
    print("X_train Shape : ", X_train.shape)
    print("X_test Shape : ", X_test.shape)
    print("Y_train Shape : ", Y_train.shape)
    print("Y_test Shape : ", X_test.shape)
  

    accurace_scores=[]
    k_values= range(1,10)

    for K in k_values:
        model=KNeighborsClassifier(n_neighbors=K)
        model.fit(X_train, Y_train)
        Y_pred=model.predict(X_test)
        accuracy=accuracy_score(Y_test,Y_pred)
        accurace_scores.append(accuracy)

    print("Accuracy report of all k values from 1 to 20")
    for value in accurace_scores:
        print(value)


def main():
    Predictor("PlayPredictor.csv")

if __name__=="__main__":
    main()