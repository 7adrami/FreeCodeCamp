import numpy as np
import pandas as pd

pd.isnull(np.nan)
pd.isnull(None)
pd.isna(np.nan)
pd.isna(None)
pd.notnull(None)
pd.notnull(np.nan)
pd.notna(np.nan)
pd.notnull(3)
pd.isnull(pd.Series([1, np.nan, 7]))
pd.notnull(pd.Series([1, np.nan, 7]))

pd.isnull(pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
}))

pd.Series([1, 2, np.nan]).count()
pd.Series([1, 2, np.nan]).sum()
pd.Series([2, 2, np.nan]).mean()

s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
pd.notnull(s)
pd.isnull(s)
pd.notnull(s).sum()
pd.isnull(s).sum()
s[pd.notnull(s)]
s.isnull()
s.notnull()
s[s.notnull()]
s.dropna()

df = pd.DataFrame({
    'Column A': [1, np.nan, 30, np.nan],
    'Column B': [2, 8, 31, np.nan],
    'Column C': [np.nan, 9, 32, 100],
    'Column D': [5, 8, 34, 110],
})

df.shape
df.info()
df.isnull()
df.isnull().sum()
df.dropna()
df.dropna(axis=1)  # axis='columns' also works

df2 = pd.DataFrame({
    'Column A': [1, np.nan, 30],
    'Column B': [2, np.nan, 31],
    'Column C': [np.nan, np.nan, 100]
})
df2

df.dropna(how='all')

df.dropna(how='any')  # default behavior
df

df.dropna(thresh=3)
df.dropna(thresh=3, axis='columns')

s.fillna(0)
s.fillna(s.mean())
s
s.fillna(method='ffill')
s.fillna(method='bfill')

pd.Series([np.nan, 3, np.nan, 9]).fillna(method='ffill')
pd.Series([1, np.nan, 3, np.nan, np.nan]).fillna(method='bfill')
df

df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()})
df.fillna(method='ffill', axis=0)

df.fillna(method='ffill', axis=1)
s.dropna().count()
missing_values = len(s.dropna()) != len(s)
missing_values
len(s)
s.count()

missing_values = s.count() != len(s)
missing_values

pd.Series([True, False, False]).any()
pd.Series([True, False, False]).all()
pd.Series([True, True, True]).all()

s.isnull()
pd.Series([1, np.nan]).isnull().any()
pd.Series([1, 2]).isnull().any()
s.isnull().any()
s.isnull().values
s.isnull().values.any()