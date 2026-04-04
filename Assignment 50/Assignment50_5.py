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
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

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

    print("Logistic Regression Accuracy : ",accuracy_score(Y_test,Y_pred_L))
    print("KNN Accuracy : ",accuracy_score(Y_test,Y_pred_K))    
    print("Random Forest Accuracy : ",accuracy_score(Y_test,Y_pred_RF))

    # confusion matrix
    print(Border)
    cm_L=confusion_matrix(Y_test,Y_pred_L)
    cm_K=confusion_matrix(Y_test,Y_pred_K)  
    cm_RF=confusion_matrix(Y_test,Y_pred_RF)

    print("Confusion matrix for Logistic Regression : ")
    print(cm_L)
    print("Confusion matrix for KNN : ")
    print(cm_K)
    print("Confusion matrix for Random Forest : ")
    print(cm_RF)

    # classification report
    print(Border)
    print("Classification report for Logistic Regression : ")
    print(classification_report(Y_test,Y_pred_L)) 

    print("Classification report for KNN : ")
    print(classification_report(Y_test,Y_pred_K))

    print("Classification report for Random Forest : ")
    print(classification_report(Y_test,Y_pred_RF))

    # ROC AUC score
    print(Border)
    print("ROC AUC score for Logistic Regression : ",roc_auc_score(Y_test,Y_pred_L))
    print("ROC AUC score for KNN : ",roc_auc_score(Y_test,Y_pred_K))
    print("ROC AUC score for Random Forest : ",roc_auc_score(Y_test,Y_pred_RF))    

    # plot confusion matrix
    plt.figure(figsize=(8,6))  
    sns.heatmap(cm_RF, annot=True, cmap='Reds')
    plt.title("Confusion Matrix for Random Forest") 
    plt.show()  

    print("ROC AUC score plot")
    from sklearn.metrics import roc_curve, auc
    fpr, tpr, thresholds = roc_curve(Y_test, Y_pred_RF)
    roc_auc = auc(fpr, tpr) 
    plt.figure()
    plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])    
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()
          

if __name__=="__main__":    
    main()