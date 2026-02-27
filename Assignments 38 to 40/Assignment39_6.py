import pandas
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

df=pandas.read_csv("student_performance.csv")

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

model=DecisionTreeClassifier(
    criterion="gini",
    max_depth=1,                                    # max_depth=3,max_depth=None,
    random_state=42
)

model.fit(X_train,Y_train)

print("model training completed")

Y_pred=model.predict(X_test)

print("Expected answer :")
print(Y_test)

print("Predicted Answer :")
print(Y_pred)

testing_Accuracy=accuracy_score(Y_test, Y_pred)

print("accuracy of mode is : " ,testing_Accuracy*100)

cm=confusion_matrix(Y_test, Y_pred)
print(cm)

