# Load dataset
data <- read.csv("data.csv")

# View data
head(data)

# Structure
str(data)

# Summary statistics
summary(data)

# Column operations
mean(data$column_name)
sum(data$column_name)

# Vector example
arr <- c(1,2,3,4)
mean(arr)