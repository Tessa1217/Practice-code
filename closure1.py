# Scope
c = 30
def func1(a):
    global c 
    print(a)
    print(c)
    c = 50 
print(c) # 30, global variable 
func1(10) # 10, 30, global variable
print(c) # 50, global variable 30 to 50 

'''Closure 

What is Closure?
Function object that "REMEMBERS" values in enclosing scopes
불변상태를 기억

Concurrency control
메모리 공간에 여러 자원이 접근 -> 교착 상태 (Dead Lock)
메모리를 공유하지 않고 메세지 전달로 처리하기 위한 ErLang

Closure in Python 
자신을 둘러싼 scope(namespace)의 상태값을 기억하는 함수 
클로저는 공유하되 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수용 프로그래밍 
클로저는 불변자료구조 및 atom, STM -> 멀티스레도(Coroutine) 프로그래밍에 강점을 제공 
''' 

class Average():
    def __init__(self):
        self._series = []
    def __call__(self, v):
        self._series.append(v)
        print('inner >> {}/{}'.format(self._series, len(self._series)))
        return sum(self._series)/len(self._series)

#First class object 
a = Average()
print(dir(a))
print(a(10))
print(a(20))
print(a(30))
print(a(40))
print(a(50))

for i in range(10, 60, 10):
    print(a(i))

class Adding():
    def __init__(self):
        self._list = []
    def __call__(self, i):
        self._list.append(i)
        return sum(self._list)

b = Adding()
print(b(1))
print(b(2))
print(b(3))
print(b(4))
print(b(5))

for i in range(1, 51):
    print(b(i))

print(sum(range(1, 51)))