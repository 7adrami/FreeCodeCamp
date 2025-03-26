import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/btc-market-price.csv')
df.head()
df = pd.read_csv('data/btc-market-price.csv', header=None)
df.columns = ['Timestamp', 'Price']
df.tail(3)
pd.to_datetime(df['Timestamp']).head()
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
df.head()
df.loc['2017-09-29']


df = pd.read_csv('data/btc-market-price.csv', header=None)
df.columns = ['Timestamp', 'Price']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

df.head()

df = pd.read_csv(
    'data/btc-market-price.csv',
    header=None,
    names=['Timestamp', 'Price'],
    index_col=0,
    parse_dates=True
)

df.head()
df.loc['2017-09-29']

df.plot()

plt.plot(df.index, df['Price'])
x = np.arange(-10, 11)
plt.plot(x, x ** 2)


plt.plot(x, x ** 2)
plt.plot(x, -1 * (x ** 2))

plt.figure(figsize=(12, 6))
plt.plot(x, x ** 2)
plt.plot(x, -1 * (x ** 2))

plt.title('My Nice Plot')
df.plot(figsize=(16, 9), title='Bitcoin Price 2017-2018')

eth = pd.read_csv('data/eth-price.csv')

eth.head()

eth = pd.read_csv('data/eth-price.csv', parse_dates=True)

print(eth.dtypes)
eth.head()

pd.to_datetime(eth['UnixTimeStamp']).head()

df.head()

pd.to_datetime(eth['Date(UTC)']).head()

pd.read_csv('data/eth-price.csv', parse_dates=[0]).head()

eth = pd.read_csv('data/eth-price.csv', parse_dates=True, index_col=0)
print(eth.info())

eth.head()

prices = pd.DataFrame(index=df.index)

prices.head()
prices['Bitcoin'] = df['Price']
prices['Ether'] = eth['Value']

prices.head()

prices.plot(figsize=(12, 6))

prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12, 6))
