import pandas

df=pandas.read_csv("student_performance.csv")

print("Total number of students in dataset are :")
print(len(df.index))

print("Average Study Hours :")
print((df["StudyHours"]).mean())

print("Average Attendance :")
print(int((df["Attendance"]).mean()))

print("Average PreviousScore :")
print(int((df["PreviousScore"]).mean()))

print("Average SleepHours :")
print(int((df["SleepHours"]).mean()))
