import pandas

df=pandas.read_csv("student_performance.csv")

print("First 5 rows are :")
print(df.head())

print("Last 5 rows are: ")
print(df.tail())

print("Total number of rows and columns are :")
print(df.shape)

print("List of column names :")
print(list(df.columns))

print("Data type of each column is :")
print(df.dtypes)
