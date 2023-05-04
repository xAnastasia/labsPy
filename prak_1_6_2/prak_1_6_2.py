#Практическое задание №1.6.2
import pandas as pd

df = pd.read_csv('house_price.csv')

numeric_dtypes = ['int64', 'float64']
numerics = []
for i in df.columns:
    if df[i].dtype in numeric_dtypes:
        numerics.append(i)
df = df[numerics]
del df['Id']
df = df.dropna()

X = df.drop('SalePrice', axis = 1)
y = df['SalePrice']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
y, test_size=0.3, random_state=42)

from sklearn.linear_model import LassoCV
lasso = LassoCV(cv=5) # Для примера возьмем cv = 5

print(lasso.fit(X_train, y_train)) # Обучаем
print(lasso.score(X_test, y_test)) # Оцениваем качество
print(lasso.coef_)