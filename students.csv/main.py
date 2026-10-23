import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\LV-PC\Desktop\Project\students.csv\students_data.csv")

df["total"] = df["math"] + df["chemistry"] + df["physics"]
 
df["Average"] = df["total"]/3
 
grade_list = []
for i in range(len(df)):
    average = df["Average"][i]

    if average >= 90:
        grade="A+"
    elif average >= 80:
        grade="A"
    elif average >= 70:
        grade="B"
    elif average >= 50:
        grade="C"
    else:
        grade="Fail"
    
    grade_list.append(grade)
df["Grade"] = grade_list

status_list = []

for i in range(len(df)):
    average = df["Average"][i]

    if average >=50:
        status = "pass"
    else:
        status = "fail"

    status_list.append(status)
df["Status"] = status_list

pass_count = (df["Status"]=="pass").sum()
fail_count = (df["Status"]=="fail").sum()
print(df["Status"].unique())

print("Total pass students:",pass_count)
print("Total fail students:",fail_count)

print("\nDepartment-Wise Student Count:")
print(df["Department"].value_counts())

marks = df["Average"].to_numpy()
print("Highest Average:",np.max(marks))
print("Lowest Average:",np.min(marks))

print("\nSubject-wise Average Marks:")

print("Math Average:", np.mean(df["math"]))
print("Chemistry Average:", np.mean(df["chemistry"]))
print("Physics Average:", np.mean(df["physics"]))

print("\nDepartment-wise Average Performance:")

department_avg = df.groupby("Department")["Average"].mean()

print(department_avg)

print("\nTop 3 student")

top_student = df.nlargest(3,"Average")
print(top_student[["Name","Department","Average","Grade"]])



    
# class average
class_average = df["Average"].mean()

print("Class Average",class_average)

topper_index = df["Average"].idxmax()
topper_name = df["Name"][topper_index]
print("Class Topper:",topper_name)

Attendance_average = df["Attendance"].mean()
print("Attendance average:",round(Attendance_average))

# final student report
print(df)
df.to_csv("Student_report.csv",index=False)
print("Student report saved succesfully")
