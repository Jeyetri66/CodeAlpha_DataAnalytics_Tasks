import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88],
    "Gender": ["M", "F", "M", "F", "M"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nHighest Marks:")
print(df.loc[df["Marks"].idxmax()])

print("\nLowest Marks:")
print(df.loc[df["Marks"].idxmin()])

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nGender-wise Average:")
print(df.groupby("Gender")["Marks"].mean())

print("\nMissing Values:")
print(df.isnull().sum())