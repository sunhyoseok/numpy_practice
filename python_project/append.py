import numpy as np

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2 = np.arange(10, 19).reshape(3, 3)
print(b2)

c2 = np.append(a2, b2) #1차원 배열로 변형
print(c2)
c2 = np.append(a2, b2, axis=0) 
print(c2)

c2 = np.append(a2, b2, axis=1) 
print(c2)