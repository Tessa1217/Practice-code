'''
파이썬 함수의 특징
1) 런타임 초기화 
2) 변수 할당 가능
3) 함수 인수 전달 가능
4) 함수 결과 반환 가능(return)

What is a first class function?
FCF - the language treats function as a value
A function that can be assigned to a variable
or passed as object/variable to other function
'''

# 팩토리얼
def factorial(n):
    '''
    Factorial function -> n : int
    '''
    if n == 1:
        return 1
    return n * factorial(n-1) # Recursion 

print(factorial(5))
'''
factorial(5):
5 * factorial(4)
4 * factorial(3)
3 * factorial(2)
2 * factorial(1) return 1
'''
print(type(factorial)) # 일급 '객체'로 취급함 
print(dir(factorial))
print('----------')
class A:
    pass
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

# 함수 factorial이 가진 성질들 
print(factorial.__name__)
print(factorial.__code__)
print(factorial.__qualname__)
print(factorial.__closure__)

# 변수에 할당이 가능한가?에 대한 증명 

func1 = factorial 
print(func1)
print(func1(10))
print(list(map(func1, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher order function)
# map, filter, reduce 

print([func1(i) for i in range(1, 6) if i%2]) 
# 함수를 결과값으로 반환에 대한 증명 

print(list(map(func1, filter(lambda x:x%2, range(1, 6))))) 
# 함수(lambda)를 필터 함수의 인자로 전달에 대한 증명

from functools import reduce 
from operator import add 
# 1부터 10까지의 합
print(sum(range(1, 11)))
# 1부터 10까지의 합 - reduce, add
print(reduce(add, range(1, 11)))
print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
