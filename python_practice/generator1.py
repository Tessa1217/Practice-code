class MyCounter():
  def __init__(self, low, high):
    self.current = low
    self.high = high 
  def __iter__(self):
    return self
  def __next__(self):
    if self.current > self.high:
      raise StopIteration 
    else:
      self.current += 1
      return self.current -1 

a = MyCounter(1, 10)
for i in a:
  print(i, end = " ")

def MyCounterGen(low, high):
  while low <= high:
    yield low 
    low += 1

for i in MyCounterGen(1, 10):
  print(i, end = " ")

# 피보나치 수열 이터레이터
class FibIterator: 
  def __init__(self, a = 1, b = 0, maxValue = 50):
    self.a = a
    self.b = b
    self.maxValue = maxValue 

  def __iter__(self):
    return self 
  
  def __next__(self):
    n = self.a + self.b 
    if n > self.maxValue:
      raise StopIteration 
    self.a = self.b
    self.b = n
    return n

for i in FibIterator():
  print(i, end = " ")

# Practice
import string 
class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self 
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration 
        value = (self.index + 1, self.data[self.index])
        self.index += 1
        return value

for index, letter in MyEnumerate(string.ascii_lowercase):
    print(f"{index}:{letter}")

# Point * Point 
class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y 
  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Point(x, y)
  def __sub__(self, other):
    x = self.x - other.x
    y = self.y - other.y
    return Point(x, y)
  def __str__(self):
    return "Point("+str(self.x)+", "+str(self.y)+")"
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)
print(p1 - p2)

# Gt
class Book:
  title = ''
  pages = 0
  def __init__(self, title = '', pages = 0):
    self.title = title
    self.pages = pages
  def __str__(self):
    return self.title
  def __gt__(self, other):
    return self.pages > other.pages
book1 = Book("Magic of Python", 600)
book2 = Book("Magic of Python", 700)
print(book1 > book2)
print(book2 > book1)

# Practice
class Circle:
    def __init__(self, radius):
        self.__radius = radius 
    def setRadius(self, radius):
        self.__radius = radius 
    def getRadius(self):
        return self.__radius 
    def __str__(self):
        return "Radius: " + str(self.__radius)
    def __add__(self, other):
        return Circle(self.__radius + other.__radius)
    def __gt__(self, other):
        return self.__radius > other.__radius 
    def __lt__(self, other):
        return self.__radius < other.__radius 

radius1 = Circle(5)
radius2 = Circle(6)
radius3 = radius1 + radius2
print(radius3)
print(radius1 > radius2)
print(radius1 < radius2)


