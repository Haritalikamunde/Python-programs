import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

X = [[25,500,12,1,2],
     [30,700,24,0,1],
     [45,1200,6,5,8],
     [50,1500,5,6,10],
     [28,600,18,1,1],
     [35,800,30,0,0],
     [48,1400,4,7,9],
     [52,1600,3,8,12],
     [27,550,20,0,1],
     [42,1300,8,4,7]]

Y = [0,0,1,1,0,0,1,1,0,1]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=45
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = MLPClassifier(
    hidden_layer_sizes=(6,),
    activation='relu',
    solver='lbfgs',
    max_iter=5000,
    random_state=42
)

model.fit(X_train_scaled, Y_train)

predictions = model.predict(X_test_scaled)

print("Actual:", Y_test)
print("Predicted:", predictions)
print("Accuracy:", accuracy_score(Y_test, predictions))

# 🔹 New prediction
new_customer = [[46,1450,5,6,9]]
new_scaled = scaler.transform(new_customer)

result = model.predict(new_scaled)
print("New Customer Prediction:", result)