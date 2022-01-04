# 1
class MyInteger():
  def __init__(self, num):
    self._num = num 
  def __add__(self, other):
    return int(self._num + other._num)
  def __repr__(self):
    return str(int(self._num))

s = MyInteger(5.00)
s2 = MyInteger(6)
print(s + s2)
print(s)

# 2
class Student():
  def __init__(self, kor, mat, eng):
    self._kor = kor
    self._mat = mat
    self._eng = eng
  def getTotal(self):
    return self._kor + self._mat + self._eng 
  def getAverage(self):
    return Student.getTotal(self)//3
  def __str__(self):
    return "국어 점수:{}\n수학 점수:{}\n영어 점수:{}\n총 점수:{}\n평균 점수:{}".format(self._kor, self._mat, self._eng, Student.getTotal(self), Student.getAverage(self))

student1 = Student(60, 100, 80)
print(student1)

# 3
class Korean():
  @staticmethod
  def printNationality():
    return "대한민국"

print(Korean.printNationality())

# 4
class Student():
  def __init__(self, name):
    self.name = name

class GraduateStudent(Student):
  def __init__(self, name, major):
    super().__init__(name)
    self.major = major 
  def __str__(self):
    return "이름: {}\n전공: {}".format(self.name, self.major)

s1 = GraduateStudent("Kim", "Psychology")
print(s1)

# 5
class CoffeeMenu():
  def __init__(self, name, price):
    self._name = name
    self._price = price
  def __str__(self):
    return "Menu name: {}\nMenu price: {}".format(self._name, str(int(self._price)))

a = CoffeeMenu("Latte", 4000.2)
print(a)

# 6
class My_Calculator:
  @staticmethod 
  def add(first_num, second_num):
    return first_num + second_num 
  @staticmethod
  def subtract(first_num, second_num):
    return first_num - second_num
  @staticmethod 
  def multiply(first_num, second_num):
    return first_num * second_num 
  @staticmethod 
  def divide(first_num, second_num):
    return first_num / second_num 

print(My_Calculator.add(3, 5))
calculator = My_Calculator()
print(calculator.add(3, 5))
