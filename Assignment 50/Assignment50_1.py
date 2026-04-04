import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

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


if __name__=="__main__":
    main()