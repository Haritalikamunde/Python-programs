import numpy
import pandas as pd
import matplotlib.pyplot as plt
import math

def EucDistance(P1, P2):
    Ans=math.sqrt((P1['X']-P2['X'])**2 + (P1['Y']-P2['Y'])**2)

    return Ans

def Predictor(new_Student):
    border ="-"*40
    data=[
            {'Student':'A', 'X':2,'Y':60,'label':'Fail'},
            {'Student':'B', 'X':5,'Y':80,'label':'Pass'},
            {'Student':'C', 'X':6,'Y':85,'label':'Pass'},
            {'Student':'D', 'X':1,'Y':50,'label':'Fail'}
        ]
    
    
    for d in data:
        d['distance']= EucDistance(d,new_Student)

    
    sorted_data=sorted(data, key=lambda item: item['distance'])
    
    print("Sorted data is :")
    for d in sorted_data:
        print(d)
    
    k=3
    nearest=sorted_data[:k]

    print("Nearest Students :")
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
    X_Student=(int(input("Enter X coordinate :")))
    Y_Student=(int(input("Enter Y coordinate :")))
    DictP['X']=X_Student
    DictP['Y']=Y_Student
    print(DictP)
    Predictor(DictP)


if __name__=="__main__":
    main()



# Explanation
# From k we decide how many values we have to check which are the closest value
# so if we take k less then it will comapre only one value and if we take K as three then it will take 3 cosest values
# and if we take k as 5 it will take closest 5 values , k helps to predict the output by comparing nearby values 
# if we take k=1 it will show wrong result beacuse it is check only one value and if we take k=5 it will check multiple values 
# more than our dataset so this will also increase error rate