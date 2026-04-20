import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Select independent and dependent variables
X = df[["x_column"]]   # independent variable
y = df["y_column"]     # dependent variable

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Plot graph
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.show()