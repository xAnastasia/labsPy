#Практическое задание №1.3.3
import pandas as pd

df = pd.read_table('wr88125.txt', sep = ';',
                   names = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall'])
print(df)

print(df.dtypes)

print(df.info())

print(df.dtypes)

df['min_t'] = df['min_t'].str.replace(' ', '')
df['average_t'] = df['average_t'].str.replace(' ', '')
df['max_t'] = df['max_t'].str.replace(' ', '')
df['rainfall'] = df['rainfall'].str.replace(' ', '')

df = df.apply(pd.to_numeric)
print(df.info())

del df['index']
print(df)

df['date'] = df['year'].astype('str') + '-' + df['month'].astype('str') + '-' + df['day'].astype('str') # самый простой способ
df['date'] = pd.to_datetime(df['date'])

print(df)

print(df.dtypes)

s = pd.Series(index = range(1960,2021), dtype = float)
for i in range(1960, 2021):
    s[i] = df[df['year'] == i].isnull().sum().sum()
print(s)
print(s.idxmax())

print(df[df['year'] == 1960].isnull().sum())

print(df[df['year'] == 1960].isnull().sum().sum())

print(df[df['year'] == 1960].isnull().sum())

df['new'] = df['max_t']-df['min_t']

s_1 = df.groupby('year')['average_t'].mean()
print(s_1.head())

print(s_1.plot())

print(s_1.idxmax())

print(s_1.idxmin())

s_2 = df.groupby('year')['rainfall'].sum()
print(s_2.head())

s_2.plot.bar(figsize = (20,3))

print(s_2.idxmax())

print(s_2.idxmin())

print(df[df['average_t'] < -30])

print(df[(df['average_t'] > 27) & (df['rainfall'] > 0.3)])