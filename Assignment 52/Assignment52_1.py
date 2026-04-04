import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def main():

    # Step 1 : EDA
    # Loading dataset
    df=pd.read_csv("student-mat.csv", sep=';')

    # Display first 5 rows 
    print("First five values are : ")
    print(df.head())

    # Display Null values
    print("Null values are : ")
    print(df.isnull().sum())

    # Display columns 
    print("Columns of dataset are ")
    print(df.columns)

    # Display Statistics
    print("Statistical report of dataset is : ")
    print(df.describe())


   

if __name__=="__main__":
    main()