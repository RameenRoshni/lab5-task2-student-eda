import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Creating student performance dataset
data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Gender": [
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Female"
    ],
    "StudyHours": [2, 5, 3, 6, 4, 7, 1, 5, 6, 3, 4, 4],
    "Attendance(%)": [82, 90, 85, 92, 88, 95, 75, 86, 94, 80, 89, 88],
    "Marks": [65, 78, np.nan, 84, 72, 91, 55, 76, 88, np.nan, 73, 72]
}
df_source = pd.DataFrame(data)
# Make the last row an exact duplicate of row 5
df_source.loc[11] = df_source.loc[4]
df_source.to_csv("student_performance.csv", index=False)
df = pd.read_csv("student_performance.csv")
# (a) Shape and info
print("Shape:", df.shape)
print("\nData information:")
df.info()
# (b) Missing values and duplicates
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
# Remove duplicate
df_clean = df.drop_duplicates().copy()
# Fill missing Marks with median
marks_median = df_clean["Marks"].median()
df_clean["Marks"] = df_clean["Marks"].fillna(marks_median)
print("\nAfter cleaning:", df_clean.shape)
print("Median used for missing Marks:", marks_median)
# (c) Histogram of Marks
plt.figure(figsize=(7, 5))
plt.hist(
    df_clean["Marks"],
    bins=6,
    edgecolor="black"
)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig("marks_histogram.png", dpi=150)
plt.close()
# Boxplot of Marks
plt.figure(figsize=(6, 5))
plt.boxplot(df_clean["Marks"])
plt.ylabel("Marks")
plt.title("Marks Boxplot")
plt.tight_layout()
plt.savefig("marks_boxplot.png", dpi=150)
plt.close()
# (d) Scatter plot: StudyHours vs Marks
plt.figure(figsize=(7, 5))
plt.scatter(
    df_clean["StudyHours"],
    df_clean["Marks"]
)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.savefig("studyhours_vs_marks.png", dpi=150)
plt.close()
# Full numeric correlation matrix
numeric_columns = [
    "StudyHours",
    "Attendance(%)",
    "Marks"
]
correlation_matrix = df_clean[numeric_columns].corr()
print("\nCorrelation matrix:")
print(correlation_matrix)
# (e) Group by Gender
gender_summary = df_clean.groupby("Gender")[
    ["Marks", "Attendance(%)"]
].mean()
print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)
print(
    "\nSaved marks_histogram.png, "
    "marks_boxplot.png, studyhours_vs_marks.png"
)