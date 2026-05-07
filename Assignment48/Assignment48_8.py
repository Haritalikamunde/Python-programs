import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

def main():

    Y_actual=[1,1,1,1,0,0,0,0]
    Y_predicted=[1,1,0,1,0,1,0,0]

    TP = TN = FP = FN = 0

    for actual, predicted in zip(Y_actual, Y_predicted):
        if actual == 1 and predicted == 1:
            TP += 1
        elif actual == 0 and predicted == 0:
            TN += 1
        elif actual == 0 and predicted == 1:
            FP += 1
        elif actual == 1 and predicted == 0:
            FN += 1

    print("True Positive (TP):", TP)
    print("True Negative (TN):", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)


if __name__=="__main__":
    main()
