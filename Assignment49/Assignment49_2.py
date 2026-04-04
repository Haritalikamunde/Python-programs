import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def main():

    # Step 1 : EDA
    # Loading dataset
    df=pd.read_csv("diabetes.csv")

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


    # print("Distribution of the target variable : ")
    # plt.figure(figsize=(8, 5))
    # sns.kdeplot(df['Outcome'], fill=True)
    # plt.title('Density Plot of Target Variable')
    # plt.xlabel('Target Variable Value')
    # plt.show()

    # Step 2: Data Preprocessing

    # Check Missing values 
    print("Missing values in columns : ")
    print(df.isna().sum())

    # Applying scaling 

    X=df.drop("Outcome", axis=1)
    Y=df["Outcome"]

    print("MinMax scaling")
    scalar=MinMaxScaler()
    X_scaled=scalar.fit_transform(X)

    print("Standard scaling")
    scalar=StandardScaler()
    X_scaled=scalar.fit_transform(X)


if __name__=="__main__":
    main()