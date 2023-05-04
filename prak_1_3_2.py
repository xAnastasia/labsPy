#Практическое задание №1.3.2

import pandas as pd

s = pd.Series(range(1,6), index = ['a', 'b', 'c', 'd', 'e'])
print(s)

print(s['d'])

print(s[1])

s['f'] = 6
print(s)

print(s['c':'e'])

df = pd.DataFrame([[1, 2], [5, 3], [3.7, 4.8]], columns = ['col1', 'col2'])
print(df)

print(df['col1'][2])

df['col2'][1] = 9
print(df)

print(df[1:3])

df['col3'] = df['col1']*df['col2']
print(df)