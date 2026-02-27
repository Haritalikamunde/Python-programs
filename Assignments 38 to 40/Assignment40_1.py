import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

df=pd.read_csv("student_performance.csv")

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
    max_depth=3,
    random_state=42
)

model.fit(X_train,Y_train)

print("model training completed")

Y_pred=model.predict(X_test)

print("Expected answer :")
print(Y_test)

print("Predicted Answer :")
print(Y_pred)

Accuracy=accuracy_score(Y_test, Y_pred)
print("accuracy of mode is : " ,Accuracy*100)

importance= model.feature_importances_

for i, v in enumerate(importance):
    print(f'Feature :{i},Score {v:.5f}')
plt.bar([x for x in range(len(importance))], importance)
plt.show()


# Conclusion
# This shows that the Attendance column has contributed most and 
# all other contributed the least for predicting result
