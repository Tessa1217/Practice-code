# Closure2

'''class Average():
    def __init__(self):
        self._series = []
    def __call__(self, v):
        self._series.append(v)
        print('inner >> {}/{}'.format(self._series, len(self._series)))
        return sum(self._series)/len(self._series)'''


def closure_1():
    # Free Variable 
    series = []
    def average(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series)/len(series)
    return average 

avg_closure1 = closure_1()
print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))
print(avg_closure1(40))
print(avg_closure1(50))

'''class Adding():
    def __init__(self):
        self._list = []
    def __call__(self, i):
        self._list.append(i)
        return sum(self._list)'''

def closure_2():
    lists = []
    def addition(i):
        lists.append(i)
        return sum(lists)
    return addition

add_closure1 = closure_2()
print(add_closure1)
print(add_closure1(1))
print(add_closure1(2))
print(add_closure1(3))
print(add_closure1(4))
print(add_closure1(5))

print(dir(avg_closure1))
print(dir(add_closure1))
print(dir(avg_closure1.__code__))
# closure1의 자유 변수 
print(avg_closure1.__code__.co_freevars)
# free varoable의 값
print(avg_closure1.__closure__[0].cell_contents)
#[10, 20, 30, 40, 50]
print(add_closure1.__closure__[0].cell_contents)
#[1, 2, 3, 4, 5]


# Scope2 
# Unbound Local Error: local variable referenced before assignment 

# def closure_1_1():
#     cnt = 0 
#     total = 0
#     def average(v):
#         cnt += 1
#         total += v
#         return total/cnt
#     return average

def closure_1_1():
    cnt = 0 
    total = 0
    def average(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total/cnt
    return average

a = closure_1_1()
print(a(10))
print(a(20))
print(a(30))