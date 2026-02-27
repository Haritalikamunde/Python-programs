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
    max_depth=1,                                    
    random_state=42
)

model.fit(X_train,Y_train)

print("model training completed")

Y_pred=model.predict(X_test)

# "StudyHours"=6,"Attendance"=85,"PreviousScore"=66,"AssignmentsCompleted"=7,"SleepHours"=7

NewTest=[[6,85,66,7,7]]

NewTestP=model.predict(NewTest)

print(NewTestP)

#Conclusion 
# as result is 1 student will pass 