#Практическое задание №1.6.1
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

X = np.array([258.0, 270.0, 294.0, 320.0, 342.0, 368.0, 396.0, 446.0, 480.0, 586.0])[:, np.newaxis]
y = np.array([236.4, 234.4, 252.8, 298.6, 314.2, 342.2, 360.8, 368.0, 391.2, 390.8])

print(X)

plt.scatter(X, y)
# plt.show()

lr = LinearRegression()
print(lr.fit(X, y))

X_ = np.arange(250, 600, 10)[:, np.newaxis]
y_lr = lr.predict(X_)

plt.scatter(X, y)
plt.plot(X_, y_lr)
# plt.show()

pr = LinearRegression()

quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X)

print(X_quad)

print(pr.fit(X_quad, y))

y_pr = pr.predict(quadratic.fit_transform(X_))

plt.scatter(X, y, label = 'тренировочные точки')
plt.plot(X_, y_lr, label = 'линейная подгонка')
plt.plot(X_, y_pr, label = 'квадратичная подгонка')
plt.legend(loc='upper left')
# plt.show()

y_pred = lr.predict(X)
print('Для линейной регрессии:', mean_squared_error(y, y_pred))

y_pred = pr.predict(X_quad)
print(y_pred)

a = pr.score(X_quad,y)
print(a)

b = lr.score(X, y)

x = np.array([10, 12, 15, 20, 25, 30, 34, 40, 47, 54, 57])[:, np.newaxis]
y = np.array([80, 75, 70, 63, 65, 70, 76, 85, 90, 92, 87 ])

plt.scatter(x, y)
# plt.show()

X_ = np.arange(10,58,1) [:, np.newaxis]

d = [2,5,7,11,15]
model = LinearRegression()
plt.figure(figsize=(15, 10))



for i in d:
  poly = PolynomialFeatures(degree = i)
  X_poly = poly.fit_transform(X)
  model.fit(X_poly,y)
  X_poly_ = poly.fit_transform(X_)
  y_pred = model.predict(X_poly_)
  print("degree = ", i,"R2:", model.score(X_poly, y))
  plt.plot(X_, y_pred, label = 'degree='+ str(i))
