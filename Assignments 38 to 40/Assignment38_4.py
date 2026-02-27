import pandas

df=pandas.read_csv("student_performance.csv")

print("Final ressult distribution :")
print(df["FinalResult"].value_counts())


students_pass=(df["FinalResult"]==1).sum()
print("Paas Students are :",students_pass)
TotalStudents=len(df.index)
TotalResult=(students_pass/TotalStudents)*100
print("percentages of pass and fail")
print(TotalResult)


students_fail=(df["FinalResult"]==0).sum()
print("Failed students are: ",students_fail)
TotalStudents=len(df.index)
TotalResult=(students_fail/TotalStudents)*100
print("percentages of failed students")
print(TotalResult)


# Dataset is not balanced as we can see there are 40% students are passed and 40% students are failed 
# so number of passed students are more than number of failed students 
# dataset is known as balanced if dataset has 50-50 equal data values