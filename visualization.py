import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

try:
    df = pd.read_csv("data.csv")
    if df.empty or 'x' not in df.columns or 'y' not in df.columns:
        df = pd.DataFrame({'x': range(10), 'y': range(10, 20)})
except Exception:
    df = pd.DataFrame({'x': range(10), 'y': range(10, 20)})

# 1. Matplotlib.pyplot: figure, plot, title, xlabel, show
plt.figure()
plt.plot(df["x"], df["y"])
plt.title("Line Plot Matplotlib")
plt.xlabel("X")
# plt.show() # Commented out to prevent blocking when running

# 2. Seaborn: set_theme, scatterplot, histplot, boxplot, kdeplot
sns.set_theme()
sns.scatterplot(data=df, x="x", y="y")
sns.histplot(data=df, x="y")
sns.boxplot(data=df, y="x")
sns.kdeplot(data=df, x="x")
# plt.show()

# 3. Plotly Express: scatter, line, histogram, box, bar
fig1 = px.scatter(df, x="x", y="y", title="PX Scatter")
fig2 = px.line(df, x="x", y="y")
fig3 = px.histogram(df, x="y")
fig4 = px.box(df, y="y")
fig5 = px.bar(df, x="x", y="y")
# fig1.show()

# 4. Plotly.graph_objects: Figure, Scatter, Bar, add_trace, update_layout
fig_go = go.Figure()
scatter_go = go.Scatter(x=df["x"], y=df["y"], mode='lines')
bar_go = go.Bar(x=df["x"], y=df["y"])
fig_go.add_trace(scatter_go)
fig_go.update_layout(title="GO Plot")
# fig_go.show()

# 5. Altair: Chart, mark_point, mark_line, encode, interactive
chart = alt.Chart(df).mark_point().encode(x='x', y='y')
chart_line = alt.Chart(df).mark_line().encode(x='x', y='y')
chart_bar = alt.Chart(df).mark_bar().encode(x='x', y='y')
chart_interactive = chart.interactive()
# chart_interactive.show()

print("Visualization tests completed.")