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