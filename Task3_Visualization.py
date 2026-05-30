import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88],
    "Gender": ["M", "F", "M", "F", "M"]
}

df = pd.DataFrame(data)

sns.barplot(x="Name", y="Marks", data=df)
plt.title("Student Marks")
plt.savefig("bar_chart.png")
plt.show()