import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score, recall_score, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier

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

    # Model Building

    # Split Dataset

    X_train, X_test, Y_train, Y_test = train_test_split( X_scaled, Y, random_state=42, test_size=0.2)

    # model= LogisticRegression(random_state=42)

    # model.fit(X_train, Y_train)

    # Y_pred= model.predict(X_test)

    # accuracy=accuracy_score(Y_test, Y_pred)
    # print("accuracy is : ", accuracy)

    model= DecisionTreeClassifier(criterion="gini",max_depth=5, random_state=42)

    model.fit(X_train, Y_train)

    Y_pred= model.predict(X_test)

    accuracy=accuracy_score(Y_test, Y_pred)
    print("accuracy is : ", accuracy)

    # for i in range(1,20):

    #     model= KNeighborsClassifier(n_neighbors=i)

    #     model.fit(X_train, Y_train)

    #     Y_pred= model.predict(X_test)

    #     accuracy=accuracy_score(Y_test, Y_pred)
    #     print("accuracy is : ", accuracy)

    print("Confusion matrix")
    print(confusion_matrix(Y_test, Y_pred))

    print("precision")
    print(precision_score(Y_test, Y_pred))

    print("recall")
    print(recall_score(Y_test, Y_pred))

    print("F1 score")
    print(f1_score(Y_test, Y_pred))

    cm = confusion_matrix(Y_test, Y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class A', 'Class B'])
    disp.plot(cmap=plt.cm.Blues)
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels="class A", yticklabels="class B")

    plt.title('Confusion Matrix')
    plt.ylabel('Actual Label')
    plt.xlabel('Predicted Label')
    plt.show()


if __name__=="__main__":
    main()