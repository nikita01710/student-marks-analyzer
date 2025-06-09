import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
with open("marks.csv","w") as f:
	f.write("name,physics,chemistry,maths\n")
	f.write("manisha,88,91,92\n")
	f.write("nisha,89,34,25\n")
	f.write("mahesh,77,89,99\n")
df=pd.read_csv("marks.csv")
print("original data:\n",df)	
df["averages"]=df[["physics","chemistry","maths"]].mean(axis=1)
print("with averages:\n",df)
highest=df["averages"].max()
lowest=df["averages"].min()
print(f"highest marks average is :{highest:0.2f}\n")
print(f"lowest marks average is :{lowest:0.2f}\n")
df["status"]=np.where((df[["physics","chemistry","maths"]]>=40).all(axis=1),"pass","fail")
print("table with status:\n",df)
pass_count=(df["status"]=="pass").sum()
fail_count=(df["status"]=="fail").sum()
print(f"number of students passed:{pass_count}\n")
print(f"number of students failed:{fail_count}\n")
plt.figure(figsize=(8,5))
plt.bar(df["name"],df["averages"],color="skyblue")
plt.xlabel("student name")
plt.ylabel("average marks")
plt.xticks(rotation=45)
plt.ylim(0,100)
plt.tight_layout()
plt.show()
subjects = ["physics", "chemistry", "maths"]

for i in range(len(df)):
    student = df.iloc[i]
    name = student["name"]
    marks = [student["physics"], student["chemistry"], student["maths"]]  

    plt.figure(figsize=(6, 4))
    plt.bar(subjects, marks, color=["green", "blue", "orange"])
    plt.title(f"{name}'s Subject-wise Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()
