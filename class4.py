# 클래스 매직

class Fruit():

  def __init__(self, name, price):
    self._name = name
    self._price = price

  def __str__(self):
    return "Fruit Class Info: {}, {}".format(self._name, self._price)

  def __add__(self, other):
    total = self._price + other._price
    if total < 10000:
      return total
    return total * 0.8 # 10000 넘으면 20% 할인

  def __sub__(self, other):
    return self._price - other._price

  def __le__(self, other):
    if self._price <= other._price:
      return True 
    else:
      return False 
      
  def __ge__(self, other):
    if self._price >= other._price:
      return True 
    else:
      return False 

# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Apple", 5000)

# 일반적인 계산
print(s1._price + s2._price)

# add 메소드 
print(s1 + s2)
print(s2 - s1)
print(s1 <= s2)
print(s1 >= s2)

class Vector(object):
  def __init__(self, *args):
    '''
    Create a vector, example: v = Vector(1, 2)
    '''
    if len(args) == 0:
      self._x, self._y = 0, 0
    else:
      self._x, self._y = args
    
  def __repr__(self):
    '''
    Return the vector information
    '''
    return "Vector(%r, %r)" %(self._x, self._y)
  
  def __add__(self, other):
    '''
    Return the vector addition of self and other
    '''
    return Vector(self._x + other._x, self._y + other._y)
  
  def __sub__(self, other):
    '''
    Return the vector subtraction of self and other
    '''
    return Vector(self._x - other._x, self._y - other._y)
  
  def __mul__(self, y):
    return Vector(self._x * y, self._y * y)
  
  def __bool__(self):
    return bool(max(self._x, self._y))


# 백터 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 출력
print(v1, v2, v3)
print(v1 + v2)
print(v2 - v1)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))

# NamedTuple
# 파이썬 데이터 모델 추상화 
# 객체 = 파이썬의 데이터를 추상화

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt 
l_leng1 = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
print(l_leng1)


from collections import namedtuple #키나 인덱스 둘 다로 접근 가능

# 네임드 튜플 선언

Point = namedtuple("Point", "x, y")

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3.y) # Key
print(pt3[1]) # Index
print(pt4) # Point(x = 2.5, y = 1.5)

l_leng2 = sqrt((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2)
print(l_leng2)


# 네임드 튜플 선언 방법

#1.
Point1 = namedtuple("Point", "x y")
#2.
Point2 = namedtuple("Point", ['x', 'y'])
#3.
Point3 = namedtuple("Point", "x, y")
#4.
Point4 = namedtuple("Point", "x, y, x, class", rename = True) # 에약어 또는 중복되는 키가 있으면 네임드 튜플이 생성되지 않음. 그럴 때 사용 하는 것이 rename
# Default = False, True로 바꿔되면 생성 가능 

print(Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x = 10, y = 35)
print(p1)
p2 = Point2(20, 40)
print(p2)
p3 = Point3(45, y=20)
print(p3)
p4 = Point4(10, 20, 30, 40)
print(p4)
