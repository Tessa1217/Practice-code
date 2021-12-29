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


