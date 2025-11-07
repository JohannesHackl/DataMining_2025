import pandas as pd

# 1
df = pd.read_csv("damin2025\lecture02\exercises\data\sales_data.csv")

# 2
print(df.shape)
print(df.head())

# 3 - total sales for each product
# Calc revenue per sale
# df['Revenue'] = df['Quantity Sold'] * df['Sales Amount']
# total revenue per product
total_sales_per_product = df.groupby('Product')['Sales Amount'].sum()
print(f'\nTotal Sales per product: {total_sales_per_product}')

# 4 - day with highest sales
daily_sales = df.groupby('Date')['Sales Amount'].sum()
best_day = daily_sales.idxmax()
highest_sales = daily_sales.max()
print(f"\nDay with Highest Sales: {best_day} with Revenue: {highest_sales}\n")

# 5  - statistics
print('\nSummary Statistics:')
# print(df['Sales Amount'].describe())

print(df.describe())
