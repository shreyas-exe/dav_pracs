import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# View data
print(df.head())

# Basic info
print(df.info())

# Summary statistics
print(df.describe())

# Column operations
print(df["column_name"].mean())
print(df["column_name"].sum())

# Numpy example
arr = np.array([1, 2, 3, 4])
print(np.mean(arr))