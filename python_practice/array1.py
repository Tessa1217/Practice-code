import numpy as np
a = np.arange(5)
print(a)

# array indexing
a = np.array([[1, 2, 3, 4, 5],[6, 7, 8], [9, 10, 11]])
print(a[0])

# creating array 
a = np.zeros(4)
print(a)

a = np.ones(2)
print(a)

a = np.empty(3)
print(a)

a = np.arange(1, 10, 2)
print(a)

a = np.linspace(0, 10, num =6)
print(a)

# Specifying data type 
a = np.ones(2, dtype=np.int64)
print(a)

# Sort array
a = np.array([2, 1, 5, 9, 8, 5, 3, 5])
a = np.sort(a)
print(a) 

a = np.array([[1, 3], [2, 5]])
a1 = np.sort(a)
a2 = np.sort(a, axis=None)
a3 = np.sort(a, axis=0)
print(a1)
print(a2)
print(a3)

dtype = [('name', 'S10'), ('age', int), ('movie', 'S10')]
values = [('Iron Man', 35, 'Avengers'), ('Superman', 28, 'Superman Returns'), ('Joker', 32, 'Batman')]
a = np.array(values, dtype=dtype)
print(np.sort(a, order='age'))
print(np.sort(a, order='movie'))

# Concatenate 
a = np.array([1, 2, 3, 4])
b = np.array([4, 5, 6, 7, 8])
c = np.concatenate((a, b))
print(c)

# Dimensions, Size, Shape
a = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],[[0, 1, 2, 3], [4, 5, 6, 7]]])
print(a.ndim)
print(a.size)
print(a.shape)

# Reshape
a = np.arange(9)
b = a.reshape(3, 3)
print(b)

# Indexing and Slicing
a = np.array([1, 2, 3, 4])
print(a[1])
print(a[0:3])
print(a[1:])

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 7])
print(a[a > 9])
print(a[a%2 == 0])
print(a[a%2!=0])
print(a[(a > 3) | (a > 7)])
print(a[(a >= 3) & (a < 10)])
b = (a > 4) | (a == 4)
print(b)

# vstack
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])
a3 = np.vstack((a1, a2))
print(a3)
a4 = np.hstack((a1, a2))
print(a4)
