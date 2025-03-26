import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales = pd.read_csv(
    'C:/Users/dell/Desktop/FreeCodeCamp/sales_data.csv',
    parse_dates=['Date'])

sales.head()

sales.shape

sales.info()

sales.describe()

sales['Unit_Cost'].describe()

sales['Unit_Cost'].mean()

sales['Unit_Cost'].median()

sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))

sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde

ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')

ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')

sales['Age_Group'].value_counts()

sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))

ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6))
ax.set_ylabel('Number of Sales')

corr = sales.corr()

corr

fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical');
plt.yticks(range(len(corr.columns)), corr.columns);

sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))

sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))

ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
ax.set_ylabel('Profit')

boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']

sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))

sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

sales['Revenue_per_Age'].head()

sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))

sales['Revenue_per_Age'].plot(kind='hist', figsize=(14,6))

sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

sales['Calculated_Cost'].head()

sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))

sales['Revenue'].plot(kind='hist', bins=100, figsize=(14,6))

sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & (sales['Country'] == 'United States'), 'Revenue'].mean()