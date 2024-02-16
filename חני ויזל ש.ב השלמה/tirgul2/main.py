import numpy as np
import pandas as pd
import sns as sns
import matplotlib.pyplot as plt
import seaborn as sn

# Create a NumPy array with values from 1 to 10
my_array = np.arange(1, 11)
random_matrix = np.random.rand(3, 3)
zeros_array = np.zeros(20)
ones_array = np.ones(10)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
my_array = np.array([1, 5, 3, 7, 2, 9])

maximum_value = np.max(my_array)
minimum_value = np.min(my_array)
result = array1 - array2
sorted_array = np.sort(my_array)
my_array[my_array % 2 == 0] = -1
nonzero_indices = np.nonzero(my_array)
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emily'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
}

df = pd.DataFrame(data)
df.rename(columns={'Name': 'Full Name', 'Age': 'Age in Years', 'City': 'Residence'}, inplace=True)
unique_names = df['Full Name'].unique()
#sns.countplot(data=df, x='X')
#sns.pairplot(df)
#sns.violinplot(data=df, x='X', y='Y')
time_series_data = pd.date_range(start='2023-01-01', periods=10, freq='D')
time_series_df = pd.DataFrame({'Date': time_series_data, 'Value': range(10)})
#sns.lineplot(data=time_series_df, x='Date', y='Value')
#g = sns.FacetGrid(df, col='X')

population = pd.Series(data)
print("DataFrame:")
print(df)

print("Sorted array:", sorted_array)
print("Maximum value:", maximum_value)
print("Minimum value:", minimum_value)
print(zeros_array)
print(ones_array)
print(random_matrix)
print(my_array)
population_dict = {'CountryA': [100, 150, 200], 'CountryB': [50, 75, 100]}
population = pd.Series(population_dict)
#inner_cells = data.iloc[1:3, 1:3]
#value_counts = data['Age'].value_counts()
#value_at_position = data.iloc[1, 2]
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 7, 12, 9]
plt.plot(x_values, y_values)
plt.title("Simple Line Plot")
plt.plot(x_values, y_values, color='red', linestyle='dashed', linewidth=2)
plt.figure(figsize=(8, 6))
y_values2 = [5, 8, 12, 6, 10]
plt.plot(x_values, y_values, label='Line 1')
plt.plot(x_values, y_values2, label='Line 2')
plt.legend()
arr = np.array(["a", "b", "c"], dtype="U")
arr1=np.array([1,2,3])
arr2 = arr1.astype(float)
arr3= arr.view()
sizeArr = arr.size
arr4, max_val88 = np.min(arr), np.max(arr)
arr5 = np.ceil(np.random.rand(5) * 10)
arr6 = np.array([1, 2, 3, 4, 5, 6])
arr7 = np.array_split(arr6, 3)
arr8 = np.array([1.0, 2.0, np.nan, 3.0])
arr9 = np.array([1, 2, 2, 3, 3, 4, 5, 5])
arr9 = np.unique(arr9)
arr10 = np.array([True, False, True])
arr11 = np.array([False, True, False])
logical_and_arr102 = np.logical_and(arr10, arr11)
logical_or_arr102 = np.logical_or(arr10, arr11)
arr12 = np.array([[1, 2], [3, 4]])
arr13 = arr12.transpose()

column_to_drop = 'Unnamed: 0'
sales_data_dropped = data.drop(column_to_drop, axis=1)
sales_data = data.drop(column_to_drop, axis=1)
sales_data.replace({'OldValue': 'NewValue'}, inplace=True)
sales_head = data.head(3)
sales_tail = data.tail(3)
sales_copy = sales_data.copy()
sales_data_ranked = data['Quantity'].rank()
sales_data_div = data.div(10)
sales_data_count = data.count()
sales_data_add = data.add(5)




