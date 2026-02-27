import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

####################################################
# Dataset Loading
####################################################
df=pandas.read_csv("student_performance.csv")


####################################################
# Data Analysis
####################################################

print("shape of dataset : ", df.shape)
print("Column names : ", list(df.columns))

print("Missing values (Per column)")
print(df.isnull().sum())

####################################################
# Visualization
####################################################


####################################################
# Train - test split
####################################################
Festures=[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

X=df[Festures]
Y=df["FinalResult"]

print("X shape :", X.shape)
print("Y shape :",Y.shape)

X_train, X_test , Y_train, Y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

####################################################
# model training 
####################################################

model=DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train,Y_train)

print("model training completed")

####################################################
# Prediction
####################################################

Y_pred=model.predict(X_test)

print("Expected answer :")
print(Y_test)

print("Predicted Answer :")
print(Y_pred)

####################################################
# Accuracy calculation
####################################################

Accuracy=accuracy_score(Y_test, Y_pred)

print("accuracy of mode is : " ,Accuracy*100)

####################################################
# confusion matrix
####################################################

cm=confusion_matrix(Y_test, Y_pred)
print(cm)

