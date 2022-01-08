class Student:
  def __init__(self, name, student_num):
    self.name = name
    self.student_num = student_num
    self.courses = []
  def enroll(self, course_name):
    self.course_name = course_name
    self.courses.append(self.course_name)
  def __str__(self):
    return "Student name: " + str(self.name) + "\nStudent ID: " + str(self.student_num) +\
    "\nClass enrolled: " + str(self.courses)

class Course:
  def __init__(self, course_name, credit):
    self.course_name = course_name
    self.credit = credit
  def __str__(self):
    return "%s (Credit: %s)" %(self.course_name, self.credit)

class Department:
  def __init__(self, department):
    self.department = department
    self.courses = []
  def getDepartment(self, department):
    return self.department
  def add_course(self, course, credit):
    self.course = course
    self.credit = credit 
    course = Course(self.course, self.credit)
    return course
  def __str__(self):
    return "%s" %self.department + "%s" %self.courses


dept = Department("Computer")
com1 = dept.add_course("Introduction to Computer Science", 5)
math1 = dept.add_course("Calculus I", 4)
Kim = Student("Kim", 20200001)
Kim.enroll(math1)
Kim.enroll(com1)
print(Kim)