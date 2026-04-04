import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

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

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    model_L = LogisticRegression()
    model_L.fit(X_train, Y_train)

    Y_pred_L = model_L.predict(X_test)

    model_K= KNeighborsClassifier()
    model_K.fit(X_train, Y_train)
    Y_pred_K = model_K.predict(X_test) 

    rf_model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
    )
    rf_model.fit(X_train, Y_train)
    Y_pred_RF = rf_model.predict(X_test)

if __name__=="__main__":    
    main()