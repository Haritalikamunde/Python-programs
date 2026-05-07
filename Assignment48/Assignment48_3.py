import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    Data=[[25,20000],[30,40000],[35,80000]]

    scalar=StandardScaler()
    Scaled_data=scalar.fit_transform(Data)
    print(Scaled_data)


if __name__=="__main__":
    main()