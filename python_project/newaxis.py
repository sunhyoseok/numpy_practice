import numpy as np

array1 = np.arange(10)
print(array1)

print(array1)
print(array1[np.newaxis, :5])
print(array1[:5, np.newaxis])

#배열 크기 변경
array2 = np.random.randint(0, 10, (2, 5))
print(array2)


#resize
array2.resize((5, 2))
print(array2)

array2.resize((5, 5))
print(array2)
# 나머지 0으로 채워짐

array2.resize((3, 3))
print(array2)
#삭제