# Dictionary to Namedtuple

from collections import namedtuple

temp_dict = {'x': 75, 'y': 55}

# Packing
Point1 = namedtuple("Point", "x, y")
n_tuple = Point1(**temp_dict)

print(n_tuple)

print(n_tuple[0]) # Indexing

print(n_tuple.x + n_tuple.y)

# Unpacking
x, y = n_tuple 
print(x, y)

# namedtuple method "make" -> List to Namedtuple
temp = [50, 10]
a = Point1._make(temp)
print(a)

# "fields" -> inquiring field name
print(a._fields)

# "asdict()" -> ordering dictionary
print(a._asdict())
temp = Point1(10, 20)
print(temp._asdict())

# example) Students Number = 20, Class = 4 (A, B, C, D)
cls = namedtuple('cls', ['rank', 'number'])
students = [cls(rank, number) 
            for rank in 'A, B, C, D'.split(',')
            for number in [str(n) for n in range(1, 21)]]
print(students)



