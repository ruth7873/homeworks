import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


# Array Creation
# 1.
array1to10 = np.arange(1, 11)

# 2.
random_matrix = np.random.random((3, 3))

# 3.
array_zeros = np.zeros(20)

# 4.
array_ones = np.ones(10)

# 5.
evenly_spaced_values = np.linspace(0, 1, num=10)

# 6.
identity_matrix = np.eye(4)

# 7.
evenly_spaced_values_2 = np.linspace(1, 10, num=100)

# Array Operations
# 8.
array_sum = array1to10 + evenly_spaced_values_2

# 9.
array_diff = array1to10 - evenly_spaced_values_2

# 10.
array_product = array1to10 * evenly_spaced_values_2

# 11.
matrix1 = np.random.random((3, 4))
matrix2 = np.random.random((4, 2))
dot_product = np.dot(matrix1, matrix2)

# 12.
transposed_matrix = np.transpose(random_matrix)

# 13.
array_mean = np.mean(array1to10)
array_median = np.median(array1to10)
array_std = np.std(array1to10)

# 14.
reshaped_matrix = np.reshape(array1to10, (2, 5))

# 15.
array_max = np.max(array1to10)
array_min = np.min(array1to10)

# 16.
sorted_array = np.sort(array1to10)

# 17.
even_indices = np.where(array1to10 % 2 == 0, -1, array1to10)

# 18.
nonzero_indices = np.nonzero(array1to10)

# 19.
concatenated_array = np.concatenate((array1to10, evenly_spaced_values_2), axis=0)

# 20.
matrix_3x3 = np.random.random((3, 3))
determinant_3x3 = np.linalg.det(matrix_3x3)

#Pandas Exercises:
# DataFrames
# 21.
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 22], 'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data_dict)

# 22.
selected_column = df['Name']

# 23.
filtered_rows = df[df['Age'] > 25]

# 24.
df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}, inplace=True)

# 25.
column_statistics = df['Years'].describe()

# 26.
sorted_df = df.sort_values(by='Years')

# 27.
grouped_data = df.groupby('City')['Years'].mean()

# 28.
df2 = pd.DataFrame({'City': ['New York', 'San Francisco'], 'Population': [8500000, 880000]})
merged_df = pd.merge(df, df2, on='City')

# 29.
df['Birth Year'] = 2022 - df['Years']

# 30.
df_no_missing = df.dropna()

# Data Analysis
# 31. Find unique values in a column.
unique_values = df['column_name'].unique()
print("Unique values in the column:", unique_values)

# 32. Count occurrences of each value in a column.
value_counts = df['column_name'].value_counts()
print("Occurrences of each value in the column:\n", value_counts)

# 33. Calculate correlation between two columns.
correlation = df['column1'].corr(df['column2'])
print("Correlation between column1 and column2:", correlation)

# 34. Pivot a DataFrame using a specific column.
pivot_table = df.pivot_table(index='column1', columns='column2', values='value_column', aggfunc='mean')
print("Pivoted DataFrame:\n", pivot_table)

# 35. Find rows with maximum and minimum values in a column.
max_row = df[df['column_name'] == df['column_name'].max()]
min_row = df[df['column_name'] == df['column_name'].min()]
print("Row with maximum value:\n", max_row)
print("Row with minimum value:\n", min_row)

# 36. Resample a time-series DataFrame.
df['datetime_column'] = pd.to_datetime(df['datetime_column'])
resampled_df = df.resample('D').mean()
print("Resampled DataFrame:\n", resampled_df)

# Data Cleaning
# 37. Remove duplicates from a DataFrame.
df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates:\n", df_no_duplicates)

# 38. Replace missing values in a DataFrame.
df_filled = df.fillna(value)
print("DataFrame with missing values replaced:\n", df_filled)

# 39. Change data type of a column.
df['column_name'] = df['column_name'].astype(new_data_type)
print("DataFrame with updated data type:\n", df)

# 40. Remove a specific column from a DataFrame.
df_without_column = df.drop('column_name', axis=1)
print("DataFrame without the specified column:\n", df_without_column)

# Basic Plotting

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 41. Create a line plot of some data.
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# 42. Create a scatter plot.
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

# 43. Create a bar chart.
categories = ['Category A', 'Category B', 'Category C']
values = [3, 7, 5]
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

# 44. Add labels to the x and y axes.
plt.plot(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot with Axes Labels')
plt.show()

# 45. Add a title to a plot.
plt.scatter(x, y)
plt.title('Scatter Plot with Title')
plt.show()

# 46. Create a histogram.
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# 47. Add a legend to a plot.
plt.plot(x, np.sin(x), label='Sine')
plt.plot(x, np.cos(x), label='Cosine')
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Legend')
plt.show()

# 48. Customize the colors and styles of plot elements.
plt.plot(x, y, color='red', linestyle='--', marker='o', label='Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')
plt.legend()
plt.show()

# 49. Create subplots in a figure.
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 0].set_title('Subplot 1')
axes[0, 1].scatter(x, y)
axes[0, 1].set_title('Subplot 2')
axes[1, 0].bar(categories, values)
axes[1, 0].set_title('Subplot 3')
axes[1, 1].hist(data, bins=30, edgecolor='black')
axes[1, 1].set_title('Subplot 4')
plt.show()

# 50. Save a plot to a file.
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Save Plot to File')
plt.savefig('saved_plot.png')
plt.show()

# Advanced Plotting

# Sample data
data1 = np.random.randn(100)
data2 = np.random.randn(100)

# 51. Create a pie chart.
labels = ['Category A', 'Category B', 'Category C']
sizes = [30, 40, 30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()

# 52. Create a box plot.
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()

# 53. Create a 3D plot.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)
ax.scatter(x, y, z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Scatter Plot')
plt.show()

# 54. Add text annotations to a plot.
x_values = np.linspace(0, 10, 100)
y_values = np.sin(x_values)
plt.plot(x_values, y_values)
plt.text(5, 0.5, 'Annotation', fontsize=12, ha='center', va='center')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Text Annotation')
plt.show()

# 55. Plot multiple data series on the same graph.
plt.plot(x_values, np.sin(x_values), label='Sine')
plt.plot(x_values, np.cos(x_values), label='Cosine')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Data Series')
plt.legend()
plt.show()

# 56. Create a heatmap.
data_matrix = np.random.rand(5, 5)
plt.imshow(data_matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()

# 57. Add error bars to a plot.
x_values = np.linspace(0, 10, 10)
y_values = np.sin(x_values)
error = np.random.rand(10)
plt.errorbar(x_values, y_values, yerr=error, fmt='o', capsize=5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Error Bars')
plt.show()

# 58. Plot data with different scales on the same graph.
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y1-axis', color=color)
ax1.plot(x_values, y_values, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Y2-axis', color=color)
ax2.plot(x_values, np.cos(x_values), color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Plot with Different Scales')
plt.show()

# 59. Create a violin plot.
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.violinplot(data, showmeans=True)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Violin Plot')
plt.show()

# 60. Plot a time series.
time_series = np.arange('2022-01-01', '2022-01-11', dtype='datetime64[D]')
values = np.random.randn(10)
plt.plot(time_series, values, marker='o')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Time Series Plot')
plt.show()




# Assuming 'df' is your DataFrame

# 61. Create a scatter plot using Seaborn.
sns.scatterplot(x='column_x', y='column_y', data=df)
plt.title('Scatter Plot')
plt.show()

# 62. Create a bar plot using Seaborn.
sns.barplot(x='category_column', y='value_column', data=df)
plt.title('Bar Plot')
plt.show()

# 63. Create a box plot using Seaborn.
sns.boxplot(x='category_column', y='value_column', data=df)
plt.title('Box Plot')
plt.show()

# 64. Create a count plot using Seaborn.
sns.countplot(x='category_column', data=df)
plt.title('Count Plot')
plt.show()

# 65. Create a pair plot for data exploration.
sns.pairplot(df)
plt.title('Pair Plot')
plt.show()

# 66. Create a heatmap using Seaborn.
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()

# 67. Create a violin plot using Seaborn.
sns.violinplot(x='category_column', y='value_column', data=df)
plt.title('Violin Plot')
plt.show()

# 68. Create a joint plot.
sns.jointplot(x='column_x', y='column_y', data=df)
plt.suptitle('Joint Plot')
plt.show()

# 69. Create a rug plot.
sns.rugplot(x='column_x', data=df, height=0.5)
plt.title('Rug Plot')
plt.show()

# 70. Customize the appearance of Seaborn plots.
# You can customize the appearance using additional parameters in the above functions.
# For example, you can add 'hue', 'palette', 'size', etc.




# Assuming 'df' is your DataFrame

# 71. Create a swarm plot using Seaborn.
sns.swarmplot(x='category_column', y='value_column', data=df)
plt.title('Swarm Plot')
plt.show()

# 72. Create a facet grid of plots using Seaborn.
g = sns.FacetGrid(df, col='facet_column', col_wrap=4, height=3)
g.map(sns.histplot, 'value_column')
plt.suptitle('Facet Grid of Plots')
plt.show()

# 73. Create a regression plot using Seaborn.
sns.regplot(x='column_x', y='column_y', data=df)
plt.title('Regression Plot')
plt.show()

# 74. Create a distribution plot.
sns.displot(df['value_column'], kde=True)
plt.title('Distribution Plot')
plt.show()

# 75. Create a cluster map.
sns.clustermap(df.corr(), cmap='coolwarm')
plt.title('Cluster Map')
plt.show()

# 76. Create a time series plot using Seaborn.
sns.lineplot(x='datetime_column', y='value_column', data=df)
plt.title('Time Series Plot')
plt.show()

# 77. Create a point plot.
sns.pointplot(x='category_column', y='value_column', data=df)
plt.title('Point Plot')
plt.show()

# 78. Customize Seaborn themes.
sns.set_theme(style='whitegrid')
# You can customize the theme using different style parameters.

# 79. Create a pair grid of plots.
sns.pairplot(df, hue='category_column')
plt.suptitle('Pair Grid of Plots')
plt.show()

# 80. Create a residual plot using Seaborn.
sns.residplot(x='column_x', y='column_y', data=df)
plt.title('Residual Plot')
plt.show()
