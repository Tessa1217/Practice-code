# abs()
i = -20
abs(i) # 20

# all()
myList = [1, 3, 4, 6]
all(myList) # True

myList = [1, 3, 0, 6]
all(myList) # False

# any()
myList = [1, 3, 0, 6]
any(myList) #True

# bin()
y = bin(80)
y #'0b~'

# eval()
exp = input("파이썬의 수식을 입력하세요: ")
try:
   eval(exp)
except ZeroDivisionError as e:
   print(e)

x = 10
y = 5
eval("x+y")

# sum()
sum([1, 2, 3])

# len()
len("All's well that ends well.")

len([1, 2, 3, 4, 5])

# list()
s = 'abcdefg'
list(s)

t = (1, 2, 3, 4, 5, 6, 7)
list(t)

# map()
def square(n):
  return n * n

mylist = [1, 2, 3, 4, 5]
result = list(map(square, mylist))
print(result)

# dir()
dir([1, 2, 3])

# complex(real, imag)
complex(4, 2)

# max(), min()
values = [1, 2, 3, 4, 5]
max(values)
min(values)

# enumerate()
seasons = ["spring", "summer", "fall", "winter"]
list(enumerate(seasons))
list(enumerate(seasons, start = 1))

# filter()
def myfilter(x):
  return x > 3

result = filter(myfilter, (1, 2, 3, 4, 5, 6, 7, 8))
print(list(result))

# zip()
numbers = [1, 2, 3, 4]
slist = ["one", "two", "three", "four"]
list(zip(numbers, slist))

names = ["Kim", "Lee", "Park"]
scores = [100, 99, 80]
for n, s in zip(names, scores):
  print(n, s)

invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]
print((sum(persons)))
any(persons)
all(persons)
max(persons)
for i, p in zip(invitations, persons):
  print(i, p)

# sort(), sorted()
myList = [4, 5, 2, 1, 6, 8]
sorted([4, 5, 2, 1, 6, 8]) # 기존의 리스트는 변경되지 않음. 정렬된 새로운 리스트를 반환하는 내장 함수.
print(myList)

myList = [4, 5, 2, 1, 6, 8]
myList.sort()
print(myList)

sorted("The health know not of their health, but only the sick".split(), key = str.lower)

students = [('홍길동', 3.9, 20160303), ('김철수', 3.0, 20160302), ('최자영', 4.3, 20160301)]
print(sorted(students, key = lambda student: student[0])) # student 요소를 받아 인덱스 번호 안에 있는 정렬 기준으로 정렬 ex - student[2], 학번을 기준으로 정렬함
print(sorted(students, key = lambda student: student[2], reverse = True))

# Address book
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age 
  def __repr__(self):
    return "<이름: %s, 나이: %s>" % (self.name, self.age)

def keyAge(person):
  return person.age 

people = [Person("홍길동", 20), Person("김철수", 35), Person("최자영", 38)]
print(sorted(people, key = keyAge))

# lambda
f = lambda x, y: x + y
print("정수의 합: ", f(10, 20))
print("정수의 합: ", f(20, 30))

list_num = [1, 2, 3, 4, 5]
f = lambda x : 2*x
result = map(f, list_num)
print(list(result))

list_a = [1, 2, 3, 4, 5, 6]
result = filter(lambda x : x % 2 == 0, list_a)
print(list(result))

data = [(3, 100), (1, 200), (7, 300), (6, 400)]
sorted(data, key = lambda item : item[0])
print(data)

import functools
result = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(result)

#x = int(input("첫번째 정수를 입력하세요: "))
#y = int(input("두번째 정수를 입력하세요: "))
f = lambda x, y: x * y 
print("두 정수의 곱은 ", f(x, y), "입니다.")

f_temp = [0, 10, 20, 30, 40, 50]
f = lambda x : (5.0/9.0) * (x - 32.0)
c_temp = map(f, f_temp)
print(list(c_temp))

orders = [["1", "재킷", 5, 120000], ["2", "셔츠", 6, 24000], ["3", "바지", 3, 50000], ["4", "코드", 6, 300000]]
result = list(map(lambda x: (x[0], x[2] * x[3]), orders))
print(result)
