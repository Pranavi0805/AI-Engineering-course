import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Basic Plot
# A basic plot shows the relationship between two sets of values.

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure()
plt.plot(x, y)
plt.title("Basic Plot - Relationship Between X and Y")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# 2. Line Plot
# Used to show trends or changes over time.
# Example: sales over different years.

years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]

plt.figure()
plt.plot(years, sales, label="Sales Trend", marker="o")
plt.title("Line Plot - Sales Over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Since sales are increasing every year,
# the graph shows an upward trend.


# 3. Bar Chart
# Used to compare values between different categories.

categories = ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]

plt.figure()
plt.bar(categories, revenue)
plt.title("Bar Chart - Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

# Here, Clothing has the highest revenue
# and Groceries has the lowest revenue.


# 4. Scatter Plot
# Used to see the relationship between two numerical variables.
# Each point represents one observation.

hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]

plt.figure()
plt.scatter(hours_studied, exam_scores)
plt.title("Scatter Plot - Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()

# Here, scores generally increase as study hours increase,
# so there is a positive relationship.
#
# Scatter plots can also help identify outliers and clusters.
# A relationship does not always mean one variable causes the other.


# 5. Histogram
# Used to understand the distribution of numerical data.
# The data is divided into ranges called bins.

histogram_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.figure()
plt.hist(histogram_data, bins=4, edgecolor="black")
plt.title("Histogram - Distribution of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# The height of each bar shows how many values
# fall into that particular range.
#
# Histogram -> distribution
# Bar Chart -> category comparison


# Creating a Sample Dataset
# We use our own dataset instead of downloading one from the internet.

df = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Exam_Score": [50, 55, 60, 65, 70, 75, 82, 90],
    "Sleep_Hours": [8, 7, 7, 6, 6, 5, 6, 7],
    "Age": [20, 21, 20, 22, 21, 23, 22, 21],
    "Performance": [
        "Low", "Low", "Medium", "Medium",
        "Medium", "High", "High", "High"
    ]
})

print(df)


# 6. Correlation Heatmap
# Used to see how numerical columns are related to each other.

numeric_df = df.drop(columns=["Performance"])
correlation = numeric_df.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap - Numerical Variables")
plt.show()

# Correlation values range from -1 to +1.
#
# +1 -> strong positive relationship
#  0 -> little or no linear relationship
# -1 -> strong negative relationship
#
# Correlation does not prove causation.


# 7. Pair Plot
# Used to see relationships between multiple numerical variables.
# It creates several scatter plots in one figure.

sns.pairplot(df.drop(columns=["Performance"]))
plt.suptitle("Pair Plot - Numerical Variables", y=1.02)
plt.show()

# This helps us compare different numerical variables
# with each other.


# 8. Pair Plot with Hue
# hue separates the data based on a category.
# Here, Performance is used to separate the groups.

sns.pairplot(df, hue="Performance")
plt.suptitle("Pair Plot with Hue - Performance Groups", y=1.02)
plt.show()

# This helps us see whether different categories
# form different patterns or groups.


# 9. Heatmap
# A heatmap can also display a matrix of values.
# Here we create a random 5 x 5 matrix using NumPy.

random_data = np.random.rand(5, 5)

plt.figure()
sns.heatmap(random_data, annot=True, cmap="coolwarm")
plt.title("Heatmap - Random Data")
plt.show()

# annot=True displays the actual values inside the cells.


# 10. Multiple Line Plot
# Used to compare trends of different groups.

years = [2020, 2021, 2022, 2023]

product_a = [100, 130, 160, 200]
product_b = [80, 120, 150, 180]

plt.figure()
plt.plot(years, product_a, marker="o", label="Product A")
plt.plot(years, product_b, marker="o", label="Product B")

plt.title("Multiple Line Plot - Product Sales Comparison")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Here, both products show an increasing trend.
# Product A has higher sales than Product B in every year.


# 11. Subplots
# Used to display multiple plots in one figure.

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(categories, revenue)
axes[0].set_title("Bar Chart - Revenue")

axes[1].plot(years, product_a, marker="o")
axes[1].set_title("Line Plot - Sales Trend")

plt.tight_layout()
plt.show()

# axes[0] represents the first plot.
# axes[1] represents the second plot.
#
# Subplots are useful when we want to compare
# different visualizations in the same figure.


# 12. Customized Line Plot
# We can customize a plot using marker, linestyle,
# linewidth, grid, etc.

plt.figure()

plt.plot(years, product_a, marker="o", linestyle="--", linewidth=2, label="Sales"
)

plt.title("Customized Line Plot - Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# marker="o" -> shows individual data points
# linestyle="--" -> creates a dashed line
# linewidth=2 -> changes the line thickness
# legend() -> displays the label
# grid() -> adds grid lines


# Quick Revision

# Line Plot    -> Shows trends over time
# Bar Chart    -> Compares categories
# Scatter Plot -> Shows relationship between two variables
# Histogram    -> Shows distribution of numerical data
# Heatmap      -> Shows correlation or matrix values
# Pair Plot    -> Shows relationships between multiple variables
# Subplots     -> Shows multiple plots in one figure