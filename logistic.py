import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Select independent and dependent variables
X = df[["x_column"]]   # or multiple columns [["x1","x2"]]
y = df["y_column"]     # categorical (0/1)

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Plot (only works well for single feature)
plt.scatter(X, y)
plt.plot(X, model.predict_proba(X)[:,1])
plt.show()