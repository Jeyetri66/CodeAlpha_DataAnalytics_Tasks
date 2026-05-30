import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1,2,3,4,5],
    "Marks": [35,45,55,65,75]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])