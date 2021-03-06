# Class Car 
class Car:
  def __init__(self, make, model, color, price):
    self.make = make
    self.model = model
    self.color = color
    self.price = price 
  def setMake(self, make):
    self.make = make 
  def getMake(self):
    return self.make
  def getDesc(self):
    return "차량 = ("+str(self.make)+", "+str(self.model)+", "+str(self.color)+", "+str(self.price)+")"

class ElectricCar(Car):
  def __init__(self, make, model, color, price, batterySize):
    super().__init__(make, model, color, price)
    self.batterySize = batterySize 
  def setBatterySize(self, batterySize):
    self.batterySize = batterySize 
  def getBatterySize(self):
    return self.batterySize

def main():
  myCar = ElectricCar("Tisla", "Model S", "white", 10000, 0)
  myCar.setMake("Tesla")
  myCar.setBatterySize(60)
  print(myCar.getDesc())
main()

# Mutiderived
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def display(self):
    print(self.name, self.age)

class Student:
  def __init__(self, id):
    self.id = id
  def showId(self):
    return self.id

class CollegeStudent(Person, Student):
  def __init__(self, name, age, id):
    Person.__init__(self, name, age) # Self 인수도 전달 필요
    Student.__init__(self, id)

student = CollegeStudent("Kim", 22, "100001")
student.display()
print(student.showId())

# Overriding

import math

class Shape:
  def __init__(self, name):
    self.name = name
  def draw(self):
    print("draw()가 호출됨")
  def get_area(self):
    raise NotImplementedError("이것은 추상 메소드입니다.")

class Circle(Shape):
  def __init__(self, name, radius = 0):
    super().__init__(name)
    self.radius = radius 
  def draw(self):
    print("원을 그립니다.")
  def get_area(self):
    return math.pi * self.radius ** 2

class Rectangle(Shape):
  def __init__(self, name, width = 0, height = 0):
    super().__init__(name)
    self.width = width
    self.height = height
  def draw(self):
    print("사각형을 그립니다.")
  def get_area(self):
    return self.width * self.height

class Triangle(Shape):
  def __init__(self, name, width = 0, height = 0):
    super().__init__(name)
    self.width = width
    self.height = height 
  def draw(self):
    print("삼각형을 그립니다.")
  def get_area(self):
    return self.width * self.height * 0.5

shapeList = [Circle("c1", 10), Rectangle("r1", 10, 10), Triangle("t1", 10, 10)]
for s in shapeList:
  print(s.get_area())

# Polymorphism

mylist = [1, 2, 3]
print("리스트의 길이 = ", len(mylist))

s = "This is a sentence"
print("문자열의 길이 = ", len(s))

d = {"aaa" : 1, "bbb" : 2}
print("딕셔너리의 길이 = ", len(d))

# 파이썬은 위임(delegation)에 의해서 다형성을 구현. len() 함수 -> 객체의 __len_()을 호출하여 연산을 객체에 "위임"

# __repr__, __str__
class Mytime:
  def __init__(self, hour, minute, second = 0):
    self.hour = hour
    self.minute = minute
    self.second = second 
  #def __repr__(self): # __repr__() - distinct
    #return "Hour: %s" %self.hour + "\nMinute: %s" %self.minute + "\nSecond: %s" %self.second 
  def __str__(self): # __str__() - readable
    return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

time = Mytime(10, 25, 30)
print(time)

# Composition
class Card:
  shapeName = ["Club", "Diamond", "Heart", "Spade"]
  rankName = [None, "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

  def __init__(self, shape, rank):
    self.shape = shape
    self.rank = rank
  
  def __str__(self):
    return Card.shapeName[self.shape] + " " + Card.rankName[self.rank]

class Deck:
  def __init__(self):
    self.cards = []
    for shape in range(4):
      for rank in range(1, 14):
        card = Card(shape, rank)
        self.cards.append(card)
  def __str__(self):
    deck = [str(card) for card in self.cards] 
    return str(deck) 

deck = Deck()
print(deck)

# Inherit and Composition
class Person:
  def __init__(self, name, number):
    self.name = name
    self.number = number 

class Student(Person):
  def __init__(self, name, number):
    super().__init__(name, number)
    self.classes = []
  def RegisterClasses(self, course):
    self.classes.append(course)
  def __str__(self):
    return "이름 = %s" %self.name + "\n주민번호 = %s" %self.number + "\n수강과목 = %s" %self.classes 

class Teacher(Person):
  def __init__(self, name, number, salary):
    super().__init__(name, number)
    self.courses = []
    self.salary = salary 
  def HaveCourses(self, classes):
    self.courses.append(classes)
  def __str__(self):
    return "이름 = %s" %self.name + "\n주민번호 = %s" %self.number + "\n강의과목 = %s" %self.courses + "\n월급 = %s" %self.salary

Kim = Student("Kim", 901030)
Kim.RegisterClasses("Python")
Kim.RegisterClasses("Java")
print(Kim)

Kwon = Teacher("Kwon", 871010, 3000000)
Kwon.HaveCourses("Python")
print(Kwon)

# Practice

class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x 
    self.y = y
  def __str__(self):
    return "(%s, %s)" %(self.x, self.y)

class Point3D(Point):
  def __init__(self, x = 0, y = 0, z = 0):
    super().__init__(x, y)
    self.z = z 
  def __str__(self):
    return "(%s, %s, %s)" %(self.x, self.y, self.z)

print(Point3D(1, 3, 2))

# Practice

# Given class
class Address:
  def __init__(self, street, city):
    self.street = str(street)
    self.city = str(city)
  
class Person:
  def __init__(self, name, email):
    self.name = str(name) 
    self.email = str(email)

# Contact class
class Contact(Address, Person):
  def __init__(self, street, city, name, email):
    Address.__init__(self, street, city)
    Person.__init__(self, name, email)
  def __str__(self):
    return "Name: %s" %self.name + "\nCity: %s" %self.city + "\nStreet: %s" %self.street +\
    "\nEmail address: %s" %self.email 

Kim = Contact("Kim", "Seattle", "64th St", "Kim@gmail.com")
print(Kim)

# Practice - Make FraudDice

import random 
class Dice:
  def __init__(self):
    self.dice = [x for x in range(1, 6)]
  def Roll(self):
    return random.randint(1, len(self.dice) + 1)

class FraudDice(Dice):
  def __init__(self):
    super().__init__()
  def Roll(self):
    die = random.randint(1, len(self.dice) + 1)
    while die <= 3:
      die = random.randint(1, len(self.dice) + 1)
    return die
    

x = FraudDice()
x.Roll()

# Practice - Oldest cat
class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age 

class Cat(Animal):
  def __init__(self, name, age, breed):
    super().__init__(name, age)
    self.breed = breed
  def __str__(self):
    return "고양이의 이름은 %s 입니다." %self.name + "\n나이는 %s살이고 %s종 입니다" %(self.age, self.breed)

cat1 = Cat("Happy", 5, "Persian")
cat2 = Cat("Tes", 3, "Russian Blue")
cat3 = Cat("Ruby", 7, "British ShortHair")

def get_oldest_cat(*args):
  return max(args)

print(cat1) 
print(cat2) 
print(cat3) 
print("\n이중에서 가장 나이가 많은 고양이는 %s살입니다." %get_oldest_cat(cat1.age, cat2.age, cat3.age))
