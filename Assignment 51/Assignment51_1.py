import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

def main():

    # Step 1 : EDA
    # Loading dataset
    df1=pd.read_csv("Fake.csv")
    df2=pd.read_csv("True.csv")

    # Add column label
    df1['label'] = 0
    df2['label'] = 1  

    # Display first 5 rows 
    print("First five values of fake news dataset are : ")      
    print(df1.head())
    print("First five values of true news dataset are : ")
    print(df2.head())

    print("combine both datasets")
    df = pd.concat([df1, df2], ignore_index=True)
    print("Combined dataset:")
    print(df.head())

    # Display Null values
    print("Null values are : ")
    print(df.isnull().sum())

    #Drop unnecessary columns
    df.drop(['date'], axis=1, inplace=True)
    # Display columns
    print("Columns of dataset are ")
    print(df.columns)

    # Display Statistics
    print("Statistical report of dataset is : ")
    print(df.describe())

    # Feature extraction
    X=df.drop("label", axis=1)
    Y=df["label"]

    vectorizer = TfidfVectorizer()
    X_vectorized = vectorizer.fit_transform(X['text'])

    print("Shape of vectorized features: ", X_vectorized)


if __name__=="__main__":
    main()