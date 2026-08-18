import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Titanic Dataset - Exploratory Data Analysis

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)


# 1. Understanding the Data

print("\nFirst 5 rows:")
print(df.head())

print("\nShape of the dataset:")
print(df.shape)

print("\nColumn information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())


# 2. Data Cleaning

# Age has some missing values, so we fill them with the median.
# Median is useful here because it is less affected by extreme values.

df["Age"] = df["Age"].fillna(df["Age"].median())

# Embarked is categorical, so we use the most common value (mode).

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin has a lot of missing values, so we drop the column.
# Keeping a column with too many missing values may not be useful.

df = df.drop(columns=["Cabin"])

# Remove duplicate rows

df = df.drop_duplicates()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nShape after cleaning:")
print(df.shape)


# 3. Filtering Data

# Passengers who travelled in first class

first_class = df[df["Pclass"] == 1]

print("\nFirst Class Passengers:")
print(first_class.head())


# 4. Survival Analysis

# Calculate the overall survival rate

survival_rate = df["Survived"].mean()

print("\nOverall Survival Rate:")
print(survival_rate)


# Survival rate by passenger class

survival_by_class = df.groupby("Pclass")["Survived"].mean()

print("\nSurvival Rate by Class:")
print(survival_by_class)


# Bar Chart - Survival Rate by Class

plt.figure()

survival_by_class.plot(kind="bar")

plt.title("Bar Chart - Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)

plt.show()

# We can compare the survival rate of passengers
# from different classes using this chart.


# 5. Age Distribution

plt.figure()

sns.histplot(df["Age"], kde=True, bins=20)

plt.title("Histogram - Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# The histogram helps us understand how the passengers'
# ages are distributed.
#
# kde=True adds a smooth curve showing the overall
# shape of the distribution.


# 6. Age vs Fare

plt.figure()

plt.scatter(df["Age"], df["Fare"], alpha=0.5)

plt.title("Scatter Plot - Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()

# This helps us see whether there is any visible
# relationship between passenger age and fare.
#
# We can also notice some passengers paid much higher
# fares than most of the others.


# 7. Survival by Gender

survival_by_gender = df.groupby("Sex")["Survived"].mean()

print("\nSurvival Rate by Gender:")
print(survival_by_gender)


plt.figure()

survival_by_gender.plot(kind="bar")

plt.title("Bar Chart - Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)

plt.show()

# This allows us to compare survival rates
# between male and female passengers.


# 8. Survival by Class and Gender

survival_class_gender = df.groupby(
    ["Pclass", "Sex"]
)["Survived"].mean()

print("\nSurvival Rate by Class and Gender:")
print(survival_class_gender)


# Pivot table makes the result easier to read

survival_pivot = df.pivot_table(
    values="Survived",
    index="Pclass",
    columns="Sex",
    aggfunc="mean"
)

print("\nSurvival Pivot Table:")
print(survival_pivot)


# 9. Survival Count

plt.figure()

sns.countplot(
    data=df,
    x="Survived"
)

plt.title("Count Plot - Survival")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")

plt.show()

# 0 -> Did not survive
# 1 -> Survived


# 10. Passenger Class Distribution

plt.figure()

sns.countplot(
    data=df,
    x="Pclass"
)

plt.title("Count Plot - Passengers by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.show()


# 11. Correlation Heatmap

# Select only numerical columns

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# The heatmap helps us quickly identify relationships
# between numerical variables.
#
# Values close to +1 -> strong positive relationship
# Values close to -1 -> strong negative relationship
# Values close to 0  -> weak linear relationship


# 12. Age Distribution by Survival

plt.figure()

sns.boxplot(
    data=df,
    x="Survived",
    y="Age"
)

plt.title("Box Plot - Age by Survival")
plt.xlabel("Survived")
plt.ylabel("Age")

plt.show()

# A box plot helps us compare the distribution of age
# between passengers who survived and those who did not.
#
# It also helps identify possible outliers.


# 13. Fare Distribution

plt.figure()

sns.histplot(
    df["Fare"],
    bins=30,
    kde=True
)

plt.title("Histogram - Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")

plt.show()

# Most passengers paid relatively lower fares,
# while a small number of passengers paid very high fares.


# 14. Survival by Embarked Location

survival_by_embarked = df.groupby("Embarked")["Survived"].mean()

print("\nSurvival Rate by Embarked Location:")
print(survival_by_embarked)


plt.figure()

survival_by_embarked.plot(kind="bar")

plt.title("Bar Chart - Survival Rate by Embarked Location")
plt.xlabel("Embarked")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)

plt.show()

