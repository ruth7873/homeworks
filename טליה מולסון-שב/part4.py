import np as np
import numpy as np


# 3. Create a pandas Series named 'population' from the given dictionary.
population_data = {'CountryA': [10, 20, 30],
                   'CountryB': [15, 25, 35],
                   'CountryC': [5, 10, 15]}
population = pd.Series(population_data)

# 4. Load a DataFrame named 'sales_data' from a CSV file named "sales.csv".
sales_data = pd.read_csv("sales.csv")

# 5. Add an index to the 'population' Series created in question 3.
population.index = population_data.keys()

# 6. Access the population of 'CountryB' in the 'population' Series without using loc.
population_CountryB = population['CountryB']

# 7. Access the sales value in the 'June' column and 'ProductA' row of the 'sales_data' DataFrame.
sales_value = sales_data.at['ProductA', 'June']

# 8. Access the four most inner cells of the 'sales_data' DataFrame.
four_inner_cells = sales_data.iloc[-4:, -4:]

# 9. Count the occurrences of each unique value in the 'sales' column of 'sales_data' DataFrame.
occurrences = sales_data['sales'].value_counts()

# 10. Convert the list 'temperature_data' to a DataFrame named 'temperature_df'.
temperature_data = [25, 30, 35]
temperature_df = pd.DataFrame(temperature_data, columns=['Temperature'])

# Convert the dictionary 'rainfall_data' to a DataFrame named 'rainfall_df'.
rainfall_data = {'City': ['CityA', 'CityB', 'CityC'], 'Rainfall': [10, 20, 30]}
rainfall_df = pd.DataFrame(rainfall_data)

# 11. Use iloc to retrieve the value in the second row and third column of the 'sales_data' DataFrame.
value_iloc = sales_data.iloc[1, 2]

# 12. Use loc to retrieve the value in the 'July' column and 'ProductB' row of the 'sales_data' DataFrame.
value_loc = sales_data.loc['ProductB', 'July']

# 13. Transpose the 'temperature_df' DataFrame.
temperature_transposed = temperature_df.transpose()

# 14. Merge the 'table1' and 'table2' DataFrames horizontally.
merged_table = pd.concat([table1, table2], axis=1)

# 15. Create a DataFrame named 'students' from the given dictionary.
students_data = {'StudentA': {'age': 20, 'grade': 'A'},
                 'StudentB': {'age': 22, 'grade': 'B'}}
students = pd.DataFrame.from_dict(students_data, orient='index')

# 16. Create a DataFrame named 'random_data' with three columns filled with random values using NumPy.
random_data = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])

# 17. Load a DataFrame named 'json_data' from a JSON file named "data.json".
json_data = pd.read_json("data.json")

# 18. Find and print the shape of the 'sales_data' DataFrame.
shape_sales_data = sales_data.shape
print("Shape of sales_data DataFrame:", shape_sales_data)

# 19. Find and print the size (total number of elements) of the 'sales_data' DataFrame.
size_sales_data = sales_data.size
print("Size of sales_data DataFrame:", size_sales_data)

# 20. Display concise information about the 'sales_data' DataFrame.
info_sales_data = sales_data.info()
print(info_sales_data)

# 21. Generate and print descriptive statistics of the 'sales_data' DataFrame.
stats_sales_data = sales_data.describe()
print("Descriptive statistics of sales_data DataFrame:\n", stats_sales_data)

# 22. Drop the 'column_to_drop' column from the 'sales_data' DataFrame.
sales_data_dropped = sales_data.drop(columns=['column_to_drop'])

# 23. Drop the 'column_to_drop' column from the 'sales_data' DataFrame without using "=".
sales_data_dropped_without_assignment = sales_data.drop(columns=['column_to_drop'], inplace=True)

# 24. Find and print the number of unique values and the unique values in the 'category' column of the 'sales_data' DataFrame.
unique_values_category = sales_data['category'].unique()
num_unique_values_category = sales_data['category'].nunique()
print("Number of unique values in 'category':", num_unique_values_category)
print("Unique values in 'category':", unique_values_category)

# 25. Find and print the indices of the minimum and maximum values in the 'price' column of the 'sales_data' DataFrame.
min_index_price = sales_data['price'].idxmin()
max_index_price = sales_data['price'].idxmax()
print("Index of minimum value in 'price':", min_index_price)
print("Index of maximum value in 'price':", max_index_price)

# 26. Create a new column 'squared_values' in the 'sales_data' DataFrame containing the squared values of the 'quantity' column.
sales_data['squared_values'] = sales_data['quantity'] ** 2

# 27. Replace all occurrences of 'OldValue' with 'NewValue' in the 'sales_data' DataFrame.
sales_data.replace('OldValue', 'NewValue', inplace=True)

# 28. Set the 'date' column as the index of the 'sales_data' DataFrame.
sales_data.set_index('date', inplace=True)

# 29. Reset the index of the 'sales_data' DataFrame.
sales_data.reset_index(inplace=True)

# 30. Display the first 3 and last 3 rows of the 'sales_data' DataFrame.
print("First 3 rows of sales_data DataFrame:\n", sales_data.head(3))
print("Last 3 rows of sales_data DataFrame:\n", sales_data.tail(3))

# 31. Add a new column 'total_sales' to the 'sales_data' DataFrame containing the sum of 'June' and 'July' columns.
sales_data['total_sales'] = sales_data['June'] + sales_data['July']

# 32. Use iloc to select the first 2 rows and the last 2 columns of the 'sales_data' DataFrame.
selected_data = sales_data.iloc[:2, -2:]

# 33. Remove all rows with missing values in the 'sales_data' DataFrame.
sales_data_no_missing = sales_data.dropna()

# 34. Replace all values in the 'temperature' column of the 'temperature_df' DataFrame that are above 30 with 30.
temperature_df['temperature'] = temperature_df['temperature'].apply(lambda x: 30 if x > 30 else x)

# 35. Fill missing values in the 'sales_data' DataFrame with the mean of the respective column.
sales_data_filled_mean = sales_data.fillna(sales_data.mean())

# 37. Save the 'sales_data' DataFrame to a new CSV file named "new_sales_data.csv".
sales_data.to_csv("new_sales_data.csv", index=False)

# 38. Create a copy of the 'sales_data' DataFrame named 'sales_copy'.
sales_copy = sales_data.copy()

# 39. Rank the 'quantity' column in the 'sales_data' DataFrame.
sales_data['quantity_rank'] = sales_data['quantity'].rank()

# 40. Find the maximum value in each column of the 'sales_data' DataFrame.
max_values = sales_data.max()

# 41. Find the minimum value in each column of the 'sales_data' DataFrame.
min_values = sales_data.min()

# 42. Find the sum of values in each column of the 'sales_data' DataFrame.
sum_values = sales_data.sum()

# 43. Multiply each element in the 'sales_data' DataFrame by 2.
sales_data_multiplied = sales_data * 2

# 44. Calculate the absolute values for each element in the 'sales_data' DataFrame.
abs_values = sales_data.abs()

# 45. Count the number of non-null values in each column of the 'sales_data' DataFrame.
non_null_counts = sales_data.count()

# 46. Add 5 to each element in the 'sales_data' DataFrame.
sales_data_added_5 = sales_data + 5

# 47. Calculate the cumulative maximum for each column in the 'sales_data' DataFrame.
cum_max_values = sales_data.cummax()

# 48. Convert the 'date' column in the 'sales_data' DataFrame to datetime format.
sales_data['date'] = pd.to_datetime(sales_data['date'])

# 49. Bin the values in the 'temperature' column of the 'temperature_df' DataFrame into three discrete intervals: 0-10, 10-20, 20-30.
temperature_df['temperature_bins'] = pd.cut(temperature_df['temperature'], bins=[0, 10, 20, 30], labels=['0-10', '10-20', '20-30'])

# 50. Create a boolean condition for the 'sales_data' DataFrame where both 'quantity' is greater than 5 and 'price' is less than 100.
condition = (sales_data['quantity'] > 5) & (sales_data['price'] < 100)
filtered_sales_data = sales_data[condition]

# 51. Sort the 'sales_data' DataFrame based on the 'date' column in ascending order.
sorted_sales_data = sales_data.sort_values(by='date')

# 52. Group the 'sales_data' DataFrame by the 'category' column and calculate the sum of 'quantity' for each category.
grouped_sales_data = sales_data.groupby('category')['quantity'].sum()





#ex 80-105
arr1=np.linspace(1,9,5)
print(arr1)

arr2=np.ceil(np.random.randint(8,10,10))
print(arr2)

arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)

arr4=np.array(['c','h','a','n','i'],dtype='U')
print(arr4)

arr5=arr3.astype(float)
print(arr5)

arr6=arr3.view()
print(arr6)

arr7=arr3.size
print(arr7)

min,max=np.min(arr1),np.max(arr1)
print(min, max)

arr8=np.ceil(np.random.rand(5)*10)
print(arr8)

arr9=arr3[:2,0:1]
print(arr9)

arr10=arr3>1
print(arr10)

arr11=np.random.rand(5)
arr11[arr11>0.5]=0
print(arr11)

arr12=np.insert(np.array([1,5,2,8]),[1,3],[1,3.5])
print(arr12)

for X94 in np.nditer(arr12):
    print(X94)

arr13=np.array([1,2,3,4,5])
arr13=np.where(arr13>3,0,arr13)
print(arr13)

arr14=np.random.rand(3,2)
arr15=np.random.rand(2,4)
arr16=np.dot(arr14,arr15)
print(arr14)
print()
print(arr15)
print()
print(arr16)

arr17=np.array([1,2,3])
arr18=np.array([4,5,6])
arr19=np.concatenate((arr17,arr18))
print(arr19)

arr20=np.array([1,5,8,7,0])
arr21=np.sort(arr20)
print(arr21)

arr22=np.array([5,87,6,3,0,1])
arr23=np.array_split(arr22,3)
print(arr23)

arr24=np.array([5,7,8,9,5,3.1,0.3,np.nan])
print(arr24)

arr25=np.array([4,5,8,9,7,6,2,2])
arr26=np.unique(arr25)
print(arr26)

arr27=np.array([False,True,True])
arr28=np.array([True,False,False])
arr29=np.logical_and(arr27,arr28)
print(arr29)

arr30=np.logical_or(arr27,arr28)
print(arr30)

arr31=np.array([[1,2],[3,4]])
arr32=arr31.transpose()
print(arr32)

