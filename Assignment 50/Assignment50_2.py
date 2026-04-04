import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def main():

    Border="-"*50
    print(Border)

    # Step 1 : EDA
    # Loading dataset
    df=pd.read_csv("bank-full.csv", sep=';')

    # Display first 5 rows 
    print(Border)
    print("First five values are : ")
    print(df.head())

    # Display Null values
    print(Border)
    print("Null values are : ")
    print(df.isnull().sum())

    # Display columns 
    print(Border)
    print("Columns of dataset are ")
    print(df.columns)

    # Display Statistics
    print(Border)
    print("Statistical report of dataset is : ")
    print(df.describe())

    sns.countplot(x='y', data=df)
    plt.title("class distribution")
    plt.show()

    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = LabelEncoder().fit_transform(df[col])

    X=df.drop("y", axis=1)
    Y=df["y"]
    print("Standard scaling")
    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)

if __name__=="__main__":
    main()