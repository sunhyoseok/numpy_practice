import numpy as np

list_data = [1, 2, 3]
array = np.array(list_data) #numpy 형태로 바꾸기

print(array.size)
print(array.dtype)
print(array[2])

# 0부터 3까지의 배열 만들기

array1 = np.arange(4)
print(array1)

array2 = np.zeros((4, 4), dtype = float) # 4x4 matrix를 0으로 초기화하며 float 자료형을 띄도록 만듦.
print(array2)

array3 = np.ones((3, 3), dtype = str)
print(array3)

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 표준정규분포 배열 만들기
array5 = np.random.normal(0, 1, (3, 3))
print(array5)