import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("dataset_mlr.csv")

# Select multiple independent variables and one dependent variable
X = df[["Hours Studied", "Previous Scores", "Sleep Hours"]].to_numpy(dtype=float)   # multiple independent variables
y = df["Performance Index"].to_numpy(dtype=float)                  # dependent variable

# Add bias column for intercept: y = b0 + b1*x1 + b2*x2 + b3*x3
X_design = np.column_stack([np.ones(X.shape[0]), X])

# Train model from scratch using least squares
# beta = [intercept, coef1, coef2, coef3]
beta, _, _, _ = np.linalg.lstsq(X_design, y, rcond=None)

# Predict values
y_pred = X_design @ beta

# Separate coefficients and intercept to mirror sklearn output style
intercept = beta[0]
coef = beta[1:]

# Print coefficients
print(coef)
print(intercept)