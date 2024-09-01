import pandas as pd

# Create a pandas series
data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series = pd.Series(data)

# Select elements greater than 30
selected_greater_than_30 = series[series > 30]

# select equal to 20
selected_equal_to_20 = series[series == 20]

# select not equal to 40
selected_not_equal_to_40 = series[series != 40]

print('Original series:')
print(series)

print('Greater than 30')
print(selected_greater_than_30)

print('Equal to 20')
print(selected_equal_to_20)

print('Not equal to 40')
print(selected_not_equal_to_40)

# ================================================
# ================================================
a = [1, 2, 3, 4, 5]
series = pd.Series(a)
b = [5, 6, 7, 8, 9]

index = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(b, index)
print(series)

squared_series = series.apply(lambda x: x ** 4)
print(squared_series)

# ==================================================
# ==================================================

sales_data = [320, 150, 130, 570, 160, 680, 140]
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sales_series = pd.Series(sales_data, index=days_of_week)

monday_sales = sales_series['Monday']
weekend_sales = sales_series[['Saturday', 'Sunday']]

total_sales = sales_series.sum()

highest_sales_day = sales_series.idxmax()
lowest_sales_day = sales_series.idxmin()

average_sales = sales_series.mean()

significant_diff = sales_series[sales_series > average_sales + 35]
significant_days = significant_diff.index.to_list()

print('Sales series')
print(sales_data)

print('\n - Monday sales: ', monday_sales)
print('\n - Weekend sales: ', weekend_sales)
print('\n - Total sales of the week: ', total_sales)
print('\n - Highest sales day: ', highest_sales_day)
print('\n - Lowest sales day: ', lowest_sales_day)
print('\n - Average sales: ', average_sales)
print('\n - Significant days: ', significant_days)