import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df=pandas.read_csv("student_performance.csv")

sns.boxplot(x=df["Attendance"])
plt.show()

