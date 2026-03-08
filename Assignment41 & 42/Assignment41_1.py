import numpy
import pandas as pd
import matplotlib.pyplot as plt
import math

def EucDistance(P1, P2):
    Ans=math.sqrt((P1['X']-P2['X'])**2 + (P1['Y']-P2['Y'])**2)

    return Ans

def Predictor(new_point):
    border ="-"*40
    data=[
            {'point':'A', 'X':1,'Y':2,'label':'Red'},
            {'point':'B', 'X':2,'Y':3,'label':'Red'},
            {'point':'C', 'X':3,'Y':1,'label':'Blue'},
            {'point':'D', 'X':6,'Y':5,'label':'Blue'}
        ]
    
    
    for d in data:
        d['distance']= EucDistance(d,new_point)

    
    sorted_data=sorted(data, key=lambda item: item['distance'])
    
    print("Sorted data is :")
    for d in sorted_data:
        print(d)
    
    k=3
    nearest=sorted_data[:k]

    print("Nearest points :")
    for d in nearest:
        print(d)
    
    # Voting

    votes={}

    for neighbor in nearest:
        label=neighbor['label']
        votes[label]=votes.get(label,0)+1

    print(border)
    print("voting result is :")
    print(border)

    for d in votes:
        print("name: ",d, "Number of votes: ", votes[d])

    print(border)

    predicted_class=max(votes,key=votes.get)

    print("Pedicted class is : ", predicted_class)
    

def main():
    DictP={}
    X_point=(int(input("Enter X coordinate :")))
    Y_point=(int(input("Enter Y coordinate :")))
    DictP['X']=X_point
    DictP['Y']=Y_point
    print(DictP)
    Predictor(DictP)


if __name__=="__main__":
    main()