import pandas

df=pandas.read_csv("student_performance.csv")

print("Total number of students in dataset are :")
print(len(df.index))

print("Count of passed students :")
print((df["FinalResult"]==1).sum())

print("Count of failed students :")
print((df["FinalResult"]==0).sum())

