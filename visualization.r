data <- read.csv("data.csv")

# Base R - Line Plot
plot(data$x, data$y, type="l", main="Line Plot")

# Base R - Bar Plot
barplot(data$y, names.arg = data$x, main="Bar Plot")

# Base R - Histogram
hist(data$y, main="Histogram")

# Base R - Scatter Plot
plot(data$x, data$y, main="Scatter Plot")

# Using ggplot2
library(ggplot2)

ggplot(data, aes(x=x, y=y)) + geom_line()
ggplot(data, aes(x=x, y=y)) + geom_bar(stat="identity")
ggplot(data, aes(x=y)) + geom_histogram()
ggplot(data, aes(x=x, y=y)) + geom_point()