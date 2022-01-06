# 객체 지향 프로그래밍(OOP) - 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대, 개선이 힘들 수 있음, 중복 발생 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리, 코드의 재사용, 코드 중복 방지, 유지보수 가능

# "Car" 일반적인 코딩 
car_company_1 = "Ferrari"
car_detail_1 = [
   {"color":"white"},
   {"horsepower":400},
   {"price":8000}
]

car_company_2 = "BMW"
car_detail_2 = [
   {"color":"black"},
   {"horsepower":500},
   {"price":7000}
]

car_company_3 = "Mercedez"
car_detail_3 = [
   {"color":"red"},
   {"horsepower":700},
   {"price":9000}
]

# "Car" 리스트 구조
# 관리 불편, 인덱스로 접근해야 하여 실수 가능성 있음, 삭제 불편
car_company_list = ["Ferrari", "BMW", "Mercedez"]
car_detail_list = [
   {"color":"white", "horsepower":400, "price":8000},
   {"color":"black", "horsepower":500, "price": 7000},
   {"color":"red", "horsepower":700, "price":9000}
   ]
del car_company_list[1]
del car_detail_list[1] 
print(car_company_list)
print(car_detail_list)

# "Car" 딕셔너리 구조
# 코드 반복 구조, 중첩 문제(키, 키는 유일해야함)
car_dicts = [
    {"car_company":"Ferrari", "car_detail":{"color":"white", "horsepower":400, "price":8000}},
    {"car_company":"BMW", "car_detail":{"color":"black", "horsepower":500, "price": 7000}},
    {"car_company":"Mercedez", "car_detail":{"color":"red", "horsepower":700, "price":9000}}
]

del car_dicts[0]
print(car_dicts)

# "Car" 클래스 구조 - 구조 설계 후 재사용성 증가, 코드 반복 최소화 (반복 최소화로 피로도 최소화), 메소드 활용
class Car():
  def __init__(self, company, details):
    self.__company = company
    self.__details = details
  def __str__(self): # 비공식적인, 사용자 입장에서 문자열로 출력하기를 원할 경우 __str__ (사용자 레벨에서 정보 확인용)
    return "str : {} - {}".format(self.__company, self.__details) # __str__ 세팅되어 있을 시 __str__ 우선적으로 출력
  def __repr__(self): # 객체 정보까지 그대로 출력할 때는 __repr__ (개발자 레벨에서 텍스트 뿐 아니라 객체의 엄격한 타입 정보 확인용)
    return "repr : {} - {}".format(self.__company, self.__details)

car1 = Car("Ferrari", {"color":"white", "horsepower":400, "price":8000})
print(car1)
car2 = Car("BMW", {"color":"black", "horsepower":500, "price": 7000})
print(car2)
car3 = Car("Mercedez", {"color":"red", "horsepower":700, "price":9000})
print(car3)
print()
print(car1.__dict__) # 클래스 안에 뭐가 들었는지 확인할 때 속성 정보값 출력
print(dir(car1))

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
print(car_list) #__repr__로 출력, 리스트 안에서 객체 정보를 보여주기 때문

# 반복문으로 출력
for x in car_list:
  print(x) #str
  print(repr(x)) #repr로 출력



# 클래스 변수, 인스턴스 변수(self)
# 네임스페이스 (dir, __dict__)

class Car():
  """
  Car class 
  Date: 2021. 12. 30
  """
  # 클래스 변수 (모든 인스턴스가 공유)
  car_counter = 0

  def __init__(self, company, details):
    self.__company = company
    self.__details = details
    # self.car_counter = 10
    Car.car_counter += 1
  def __str__(self): 
    return "str : {} - {}".format(self.__company, self.__details) 
  def __repr__(self): 
    return "repr : {} - {}".format(self.__company, self.__details)
  def __del__(self):
    Car.car_counter -= 1
  def detail_info(self):
    print("Current ID: {}".format(id(self))) # self = car1, car2, car3
    print("Car Detail Info: {}, {}".format(self.__company, self.__details.get("price")))

# self의 의미 - 인스턴스 변수의 첫번째 매개변수 ("붕어빵 기계 - 틀은 하나지만 찍어내는 것들은 다름")
car1 = Car("Ferrari", {"color":"white", "horsepower":400, "price":8000})
car2 = Car("BMW", {"color":"black", "horsepower":500, "price": 7000})
car3 = Car("Mercedez", {"color":"red", "horsepower":700, "price":9000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1 is car2)
print(dir(car1))
print(dir(car2))

print(Car.__doc__)
print()

car1.detail_info() # id(car1) == id(self)
car2.detail_info()
car3.detail_info()

# 비교
print(car1 is car2) # False
print(car1.__class__) # True
print(car2.__class__) # True
print(car3.__class__) # True
print(id(car1.__class__)) # True(클래스 값(부모)은 동일)
print(id(car2.__class__)) # True
print(id(car3.__class__)) # True
print(car1.__class__ == car2.__class__) # True
print(id(car1.__class__) == id(car1.__class__)) # True

#에러
# Car.detail_info() 인자가 자동으로 전달되지 않기 때문에 명시적으로 전달 필요
Car.detail_info(car2)
print(Car.detail_info(car1) == Car.detail_info(car2))

# 클래스 변수 공유 확인
print(car1.__dict__) # 클래스 변수 보이지 않음
print(car2.__dict__)
print(car1.car_counter) # 클래스 변수에 접근할 경우 출력 가능
print(car2.car_counter)
print(car1.car_counter == car2.car_counter) # True

print(dir(car1)) 

# 접근
print(car1.car_counter) # 공유하고 있으므로 Car 클래스로 접근해도 가능
# self.car_counter가 인스턴스 네임스페이스에 있으므로 car1.car_counter = 10이 됨.
print(Car.car_counter)

# Del
del car2 
# 삭제 확인
print(car1.car_counter) # 2


# 인스턴스 네임스페이스에 없으면 상위에서 자동으로 검색 
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 없으면 상위 클래스 변수를 찾음)