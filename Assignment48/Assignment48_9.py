from sklearn.metrics import classification_report

def main():

    Y_actual=[1,1,1,1,0,0,0,0]
    Y_predicted=[1,1,0,1,0,1,0,0]

    report = classification_report(Y_actual, Y_predicted)

    print(report)


if __name__=="__main__":
    main()