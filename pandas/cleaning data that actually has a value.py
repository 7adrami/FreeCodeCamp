import numpy as np
import pandas as pd
df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29, 30, 24, 290, 25],
})
df
df['Sex'].unique()
df['Sex'].value_counts()
df['Sex'].replace('D', 'F')
df['Sex'].replace({'D': 'F', 'N': 'M'})

df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290: 29
    }
})
df[df['Age'] > 100]

df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10

ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])
print(ambassadors)

ambassadors.duplicated()
ambassadors.duplicated(keep='last')
ambassadors.duplicated(keep=False)
ambassadors.drop_duplicates()

ambassadors.drop_duplicates(keep='last')
ambassadors.drop_duplicates(keep=False)

players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})
print(players)
players.duplicated()
players.duplicated(subset=['Name'])
players.duplicated(subset=['Name'], keep='last')
players.drop_duplicates()
players.drop_duplicates(subset=['Name'])
players.drop_duplicates(subset=['Name'], keep='last')

df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})
print(df)
df['Data'].str.split('_')
df['Data'].str.split('_', expand=True)
df = df['Data'].str.split('_', expand=True)
df.columns = ['Year', 'Sex', 'Country', 'No Children']
df['Year'].str.contains('\?')
df['Country'].str.contains('U')
df['Country'].str.strip()
df['Country'].str.replace(' ', '')
df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'))
