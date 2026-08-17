import pandas as pd
import numpy as np
                            # Intro to pandas --powerful lib for data manipulation and analysis
# easy to use data structure which is series of data frames

series=pd.Series([10,20,30], index=["a","b","c"]) # 1D array
print(series)

data ={"Name":["Alice","Bob"], "Age":[40,30]} #--dictionary
print(data)
df=pd.DataFrame(data)  # 2D --data frame
print(df)

# To load the data from and save the data to csv or excel
# df=pd.read_csv("data.csv") # load
# df.to_csv("data.csv", index=False) # save
# df=pd.read_excel("data.xlsx")
# df.to_excel("data.csv", index=False)

# Viewing the data
print(df.head(1))
print(df.tail(1))

print(df.info())
print(df.describe()) # for stats

print("Filter by columns names:")
print(df[["Name"]])

print("Filter the rows:")
print(df[df["Age"]>30])

print("First row by position:")
print(df.iloc[0]) # gives the row by position

print("First Col by position:")
print(df.iloc[:,0]) # gives the first col by position

print("First row by label:")
print(df.loc[0])

print("First col by label:")
print(df.loc[:,"Name"])


# Example 1:

#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# Load Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore structure
print("First 5 rows: \n", df.head())
print("Last 5 rows: \n", df.tail())
print(df.describe())

selected_columns = df[["species", "sepal_length"]]
print("Selected Columns: \n", selected_columns)


filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filteres Rows: \n", filtered_rows)
#filtered_rows.to_csv("Filtered_iris.csv",index=False) -- to save the filtered rows

filtered_rows["sepal_area"] = filtered_rows["sepal_length"] * filtered_rows["sepal_width"]

# 3. Add Column using Conditional Logic (If length > 5.0, mark as Big)
filtered_rows["size_category"] = np.where(filtered_rows["sepal_length"] > 5.0, "Big", "Small")

# 4. Add Column using String Manipulation (Uppercase the species name)
filtered_rows["species_upper"] = filtered_rows["species"].str.upper()

print(filtered_rows)
#filtered_rows.to_csv("Filtered_iris.csv",index=False)

                    # DataCleaning and Preparation

#Handling Missing Values( Drop Missing Vals | Fill Missing Values | Interpolation)

#dropping:
#df=df.dropna() --drop missing rows
#df=df.dropna(axis=1) --drop missing cols

#Filling-- manually specifiying what to fill 
#df["col_name"]=df=["col_name"].fillna(0)
#df.fillna(method="ffill") --forward filling  --carries the last known value forward.
#df.fillna(method="bfill") --backwardward filling --use the next available value.

#Interpolation --estimating missing values based on the values around them. Pandas calculates an estimated value from nearby data.
#df["col_name"]=df=["col_name"].interpolate()

# ffill → look backward for a value and carry it forward
# bfill → look forward for a value and carry it backward
# interpolate → calculate what the missing value should be.

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}
df = pd.DataFrame(data)

print("Original Dataset: \n", df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

df = df.rename(columns={"Name":"Student_Name", "Score": "Exam:Score"})
print("Dataset: \n", df)

#Data Transformations(Renaming, Changing the dtypes, creating or modifying the cols)

#1. Rename Column names:
#df=df.rename(columns={"old_col_name":"new_col_name"})
#2. Changing Data types
#df["col_name"]=df["col_name"].astype("float") --converting to float
#df["col_name"]= pd.to_datetime(df["col_name"]) --converting and string type date to date type
#3. ceating or modifying the columns
#df["new_col"]=df["col_name"]* 24.5 --adding a new col having modified vals of the col_name(existing cols)

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "salary": ["30000", "40000", "50000"],
    "joining_date": ["2024-01-10", "2024-02-15", "2024-03-20"]
})

# 1. Rename column
df = df.rename(columns={"salary": "monthly_salary"})

# 2. Change data types
df["monthly_salary"] = df["monthly_salary"].astype("float")
df["joining_date"] = pd.to_datetime(df["joining_date"])

# 3. Create a new/modified column
df["annual_salary"] = df["monthly_salary"] * 12

print(df)

#One-hot Encoding: One-hot encoding is a technique used in data preprocessing to convert categorical data (text/categories) into numerical 0s and 1s, so machine-learning models can work with it.
#using get_dummies()

df = pd.DataFrame({
    "Color": ["Red", "Blue", "Green", "Red"]
})

encoded = pd.get_dummies(df, columns=["Color"] ,dtype=int)

print(encoded)

#Combining and Merging DataFrames

#Concatenation:
#combined=pd.concat([df1,df2],axis=0) --for rows
#combined=pd.concat([df1,df2],axis=1) --for cols

#Merging --based on key or condition
#merged= pd.merge(df1,df2, on="common_col_name")
#merged= pd.merge(df1, df2, how="left or inner or right or.." on="common_col_name")

#Joining --index alignment
# joined= df1.join(df2, how="left or inner or right or..")

import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

df2 = pd.DataFrame({
    "id": [4, 5, 6],
    "name": ["David", "Emma", "Frank"]
})

df3 = pd.DataFrame({
    "id": [1, 2, 3],
    "salary": [30000, 40000, 50000]
})

# 1. Concatenation - combine rows
combined = pd.concat([df1, df2], axis=0, ignore_index=True)

# 2. Merging - combine using common column or key --similar to SQLjoin
merged = pd.merge(df1, df3, on="id", how="inner")

# 3. Joining - combine using index by default -- best usage when DataFrames have matching indexes-- index is the label used to identify each row.
joined = df1.join(df3.set_index("id"), on="id")

print("Concatenated:")
print(combined)

print("\nMerged:")
print(merged)

print("\nJoined:")
print(joined)

# Example:

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [85, 90, 88]
})

print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Score_Percentage"] = (merged["Score"] / 200) * 100
print("Transformed Dataset \n", merged)

                                        #Data Aggregation and Grouping in Pandas

#Grouping Data By Categories:
#--Why group data: allows u to perform ops on subsets of data based on shared categories
#Group similar rows together, then perform an operation on each group.
#--using groupby
#grouped=df.groupby("col_name")
#Operations:
    #Iteration:
    #for name,group in grouped:
        #print(name,group)
    #Apply Aggregation
    #grouped.mean()
    #grouped.sum()
print("Grouping Example:")
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Sales"],
    "Salary": [30000, 40000, 25000, 35000, 50000]
})

print(df)
grouped = df.groupby("Department")
print(grouped["Salary"].mean())
df.groupby("Department")["Salary"].sum()

#Aggregate Functions:

#using groupby:
#df.groupby("categorical_col")[numerical_col].mean()
#df.groupby("categorical_col").agg({"numerical_col":["mean","sum","min","max"]}) -- MultiAggregation

#using pivotTable: --reshape the data with aggregation if you use pivot table function

# pivot= df.pivot_table{
#     values= "numeric_col",
#     index= "categorical_col",
#     aggfunc="mean"
# }

#Custom Aggregation:
# def range_func(x):
#     return x.max()-x.min()
# df.groupby("categorical_col")[numerical_col].agg(range_func)

#Example:
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Marketing", "Marketing"],
    "Sales": [1050, 2100, 1500, 2550, 3050, 4500]
})

grouped = df.groupby("Department")

# 1. Groupby - Single Aggregation
print(df.groupby("Department")["Sales"].mean())

# 2. Groupby - Multiple Aggregations
print(df.groupby("Department").agg({
    "Sales": ["mean", "sum", "min", "max"]
}))

# 3. Pivot Table - Aggregation
pivot = df.pivot_table(
    values="Sales",
    index="Department",
    aggfunc="mean"
)
print(pivot)

# 4. Custom Aggregation - Range
def range_func(x):
    return x.max() - x.min()

print(df.groupby("Department")["Sales"].agg(range_func))

# 5. Custom function for variance
# Variance = average of (value - mean)²
def variance_func(x):
    mean = x.mean()
    return ((x - mean) ** 2).mean()
print(df.groupby("Department")["Sales"].agg(variance_func))