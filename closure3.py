'''

Decorator 

Advantage of using decorator
1. 중복 제거, 코드 간결, 공통 함수 작성
2. 로깅, 프레임워크, 유효성 체크 등 -> 공통 기능
3. 조합해서 사용 용이

Disadvantage of using decorator
1. 가독성
2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리
3. 디버깅 불편함 

'''

import time 

def perf_timecheck(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        start = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        end = time.perf_counter() - start
        # 실행 함수명 
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r'%(end, name, arg_str, result))
        return result 
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)

def sum_func(*numbers):
    return sum(numbers)

none_deco1 = perf_timecheck(time_func)
none_deco2 = perf_timecheck(sum_func)

print(none_deco1(1), none_deco1.__code__.co_freevars)
print(none_deco2(100, 200, 300, 400, 500), none_deco2.__code__.co_freevars)

# Decorator

@perf_timecheck
def time_func(seconds):
    time.sleep(seconds)

@perf_timecheck
def sum_func(*numbers):
    return sum(numbers)

time_func(1)
sum_func(100, 200, 300, 400, 500)


