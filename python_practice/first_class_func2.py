'''Lambda (익명함수) 
- 가급적 주석 작성 
- 가급적 함수 작성 
- 일반 함수 형태로 리팩토링 권장'''

from functools import reduce 
print(reduce(lambda x, t: x + t, range(1, 11)))

'''

Callable 
* Built-in-method checking and returning True if 
the object is callable
* 메소드 형태로 호출 가능한지 확인 

Callable object: any object that 
can be called like a function

'''

print(callable(str)) # True 
print(callable(3.14)) # False 3.14()로 호출할 수 없음 

class A:
    def a(self):
        print("A")
aa = A()
print(callable(A)) # True
print(callable(A.a)) # True
print(callable(aa)) # False Instance cannot be callable 


import inspect 
def func(x):
    x = x
print(inspect.isfunction(func)) # True

print(inspect.isclass(A)) # True

'''Partial:
* a class from functools library
* create a new function with partial application 
of the arguments and keywords
* freeze a portion of the function argument 
* ex) Partial(func, arg)
* 인수를 고정함
* 콜백 함수에 사용
'''

from operator import mul 
from functools import partial

print(mul(10, 10)) # == print(10 * 10)
five = partial(mul, 5) # partial(func, arg)
# 함수를 인자로 전달 가능하고 함수를 변수에 할당: 일급 함수의 특징
print(five(10))
six = partial(five, 6)
print(six())
# print(six(9)) Error raised: mul expected 2 args got 3

print([five(i) for i in range(1, 11)]) # 5의 배수를 구할 수 있음
print(list(map(five, range(1, 10))))

# 구구단 만들기 using Partial 
for i in range(1, 10):
    multiple = partial(mul, i)
    print([multiple(i) for i in range(1, 10)])



def solution(L:list, x:int):
    if x > L[-1]:
        L.append(x)
    elif x < L[0]:
        L.insert(0, x)
    else:
        for i in range(len(L)):
            if x < L[i]:
                L.insert(i, x)
    return L

print(solution([2, 4, 6, 8, 10], 5))

