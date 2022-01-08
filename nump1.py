# numpy
import numpy as np

ftemp = [63, 73, 53, 80, 59, 64, 34, 92, 63]
F = np.array(ftemp) 
print(F)

ctemp = [(t-32)*5/9 for t in ftemp]
C = np.array(ctemp)
print(C)

import matplotlib.pyplot as plt
plt.plot(C)
plt.xlabel("Day")
plt.ylabel("Celcius")
plt.show()

# array + array
A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])
result = A + B
print(result)

# Two D matrix
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[0][1])

for i in range(len(a)):
    for x in range(len(a)):
        print(a[i][x], end = ' ')

# Numpy speed

import numpy as np 
import time
a = [i for i in range(10000000)]
start = time.time()
a = [i + 2 for i in a]
end = time.time()
print(end - start)

a_array = np.array([i for i in range(10000000)])
start = time.time()
a_array += 2
end = time.time()
print(end - start)

