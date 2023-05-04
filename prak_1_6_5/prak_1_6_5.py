#Практическое задание №1.6.5
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn. tree import DecisionTreeClassifier
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_score



df = pd.read_csv('diabetes.csv')
df['Outcome'].value_counts()

X = df.drop('Outcome', axis=1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.3, random_state=42)

svm = SVC(kernel = 'linear')
svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)
print(classification_report(y_test, y_pred))

scale = StandardScaler()
X_scale = scale.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scale, y,
test_size=0.3, random_state=42)
svm_1 = SVC(kernel = 'linear')
svm_1.fit(X_train, y_train)
y_pred = svm_1.predict(X_test)
print(classification_report(y_test, y_pred))

svm_2 = SVC(kernel = 'linear')
cross = cross_val_score(svm_2, X, y, cv=6, scoring =
'f1_weighted')
cross_std = cross_val_score(svm_2, X_scale, y, cv=6, scoring =
'f1_weighted')
print(np.mean(cross))
print(np.mean(cross_std))

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 42)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
confusion_matrix(y_test, y_pred)
precision_recall_fscore_support(y_test, y_pred)
precision_score(y_test, y_pred)


dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
y_pred = dtc.predict(X_test)
print(classification_report(y_test, y_pred))


