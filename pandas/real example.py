import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv(
    'C:/Users/dell/Desktop/FreeCodeCamp/pandas/btc-eth-prices-outliers.csv',
    index_col=0,
    parse_dates=True
)

df.head()

df.plot(figsize=(16, 9))

df.loc['2017-12': '2017-12-15'].plot(y='Ether', figsize=(16, 9))

df.loc['2017-12': '2017-12-15'].plot(y='Ether', figsize=(16, 9))

df_na = df.loc['2017-12': '2017-12-15']

df_na['Ether'].isna().values.any()

df_na.loc[df_na['Ether'].isna()]

df.loc['2017-12-06': '2017-12-12']

df.loc['2017-12-06': '2017-12-12'].fillna(method='bfill')

df.fillna(method='bfill', inplace=True)

df.plot(figsize=(16, 9))

df['2017-12-25':'2018-01-01'].plot()

df['2018-03-01': '2018-03-09'].plot()

df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))

df_cleaned.plot(figsize=(16, 9))

df.mean()

df_cleaned.mean()

df.median()

df_cleaned.plot(kind='hist', y='Ether', bins=150)

df_cleaned.plot(kind='hist', y='Bitcoin', bins=150)

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Ether'], ax=ax)

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], rug=True, ax=ax)

fig, ax = plt.subplots(figsize=(15, 7))
sns.kdeplot(df_cleaned['Ether'], shade=True, cut=0, ax=ax)
sns.rugplot(df_cleaned['Ether'], ax=ax);

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))

sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)

fig, ax = plt.subplots(figsize=(15, 7))
sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)

df_cleaned['Bitcoin'].quantile(.2)

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.2, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.2), color='red')

df_cleaned['Bitcoin'].quantile(.5)

df_cleaned['Bitcoin'].median()

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].quantile(.5), color='red')

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df_cleaned['Bitcoin'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(df_cleaned['Bitcoin'].median(), color='red')

df['Bitcoin'].max() - df['Bitcoin'].min()

df_cleaned['Bitcoin'].max() - df_cleaned['Bitcoin'].min()

df['Bitcoin'].var()

df['Bitcoin'].std()

df_cleaned['Bitcoin'].std()

df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)

df_cleaned['Bitcoin'].quantile(.75) - df_cleaned['Bitcoin'].quantile(.25)

upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()

print("Upper Limit: {}".format(upper_limit))
print("Lower Limit: {}".format(lower_limit))

fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(df['Bitcoin'], ax=ax)
ax.axvline(lower_limit, color='red')
ax.axvline(upper_limit, color='red')



with open("C:/Users/dell/Desktop/FreeCodeCamp/pandas/btc-market-price.csv", 'r') as data:
    for index, line in enumerate(data.readlines()):
        if (index<100):
            print(index, line)