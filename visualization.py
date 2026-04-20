import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Line Plot (Matplotlib)
plt.plot(df["x"], df["y"])
plt.title("Line Plot")
plt.show()

# Bar Plot (Matplotlib)
plt.bar(df["x"], df["y"])
plt.title("Bar Plot")
plt.show()

# Histogram (Seaborn)
sns.histplot(df["y"])
plt.title("Histogram")
plt.show()

# Scatter Plot (Seaborn)
sns.scatterplot(x=df["x"], y=df["y"])
plt.title("Scatter Plot")
plt.show()