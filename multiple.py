import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data.csv")

# Select multiple independent variables and one dependent variable
X = df[["x1", "x2", "x3"]]   # multiple independent variables
y = df["y"]                  # dependent variable

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Print coefficients
print(model.coef_)
print(model.intercept_)