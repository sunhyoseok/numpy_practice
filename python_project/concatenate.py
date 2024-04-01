import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

#가로로 합치기
array3 = np.concatenate([array1, array2])
print(array3.shape)
print(array3)

#세로로 합치기

array4 = np.arange(4).reshape(1, 4)
array5 = np.arange(8).reshape(2, 4)

print(array4)
print(array5)

array6 = np.concatenate([array4, array5], axis=0)
print(array6)