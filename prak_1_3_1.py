#Практическое задание №1.3.1

import numpy as np

arr_1 = np.full((3, 4), 3)
arr_2 = np.random.randint(0, 10, (2, 4))

print(arr_1.size)
print(arr_2.size)

np.concatenate([arr_1, arr_2])

arr_3 = np.array((1, 8, 6, 5, 8, 3))
print(arr_3)

arr_4 = arr_3*3 + 1
print(arr_4)

arr_5 = arr_3.reshape((2,3))
print(arr_5)

arr_5.min(axis=1)

arr_5.mean()

arr_6 = np.array([i**2 for i in range(0,11)])
print(arr_6)

arr_6[1::2]
print(arr_6[1::2])

arr_6[::-1]
print(arr_6[::-1])

arr_6[1::2] = 2
print(arr_6)

print(49 in arr_6)

A = np.random.randint(-5, 6, (3,3))
print(A)

B = A[A<0]
print(B)