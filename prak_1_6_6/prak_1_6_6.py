#Практическое задание №1.6.6
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn. tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn. model_selection import GridSearchCV



df = pd.read_csv('winequality-red.csv')
print(df.head())
print(df.info())
df['quality']. value_counts()

X = df.drop('quality', axis = 1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)

print(classification_report(y_test, y_pred))

dtc = DecisionTreeClassifier()
dtc. fit(X_train, y_train)
y_pred = dtc. predict(X_test)
print(classification_report(y_test, y_pred))

parameters = {'n_estimators': [100, 300, 500, 1000, 1500]}
grid = GridSearchCV( rfc, parameters)
grid.fit(X_train, y_train)
print(grid.best_estimator_)