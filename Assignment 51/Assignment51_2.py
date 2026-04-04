import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from scipy.sparse import hstack

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


    vectorizer = TfidfVectorizer()
    text_v = vectorizer.fit_transform(df['text'])
    title_v = vectorizer.fit_transform(df['title'])

    X = hstack([text_v, title_v])
    Y=df["label"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model_lr=LogisticRegression()
    model_lr.fit(X_train,Y_train)
    model_lr.predict(X_test)

    model_dt=DecisionTreeClassifier(random_state=42)
    model_dt.fit(X_train,Y_train)
    model_dt.predict(X_test)

    hard_model = VotingClassifier(
        estimators=[
            ('lr',model_lr),
            ('dt',model_dt),
    
        ],
        voting='hard'
    )

    hard_model.fit(X_train,Y_train)

    pred_hard = hard_model.predict(X_test)
    acc_hard = accuracy_score(pred_hard,Y_test)

    print("Hard voting accuracy : ",acc_hard)

if __name__=="__main__":
    main()