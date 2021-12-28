# copy.deepcopy()
import copy 

colors = ["red", "blue", "green"]
a = colors
a[0] = "white"
print(colors)
print(a)

colors_1 = ["red", "blue", "green"]
b = copy.deepcopy(colors_1)
b[0] = "yellow"
print(colors_1)
print(b)

# random

import random 
print(random.randint(1, 6))

print(random.random())

ran = random.random()
print(ran * 100)

myList = ["red", "blue", "green"]
print(random.choice(myList))

myList = [ x for x in range(10) if x % 2 == 0]
random.shuffle(myList)
print(myList)

num = random.randrange(0, 101, 2)
print(num)

# time()
import time
print(time.time())

start = time.time()
myList = [ x for x in range(10) if x % 2 == 0]
random.shuffle(myList)
print(myList)
end = time.time()
print(end - start)

print(time.asctime())

yesterday = (2021, 12, 28, 1, 46, 42, 2, 0, 0)
print(time.asctime(yesterday))

import time 
for i in range(10, 0, -1):
    print(i, end = " ")
    time.sleep(3)
print("Done!")

import calendar 
cal = calendar.month(2021, 12)
print(cal)

# practice 
import time 
def fib(n):
    a, b = 0, 1
    while n > b:
        print(b, end = " ")
        a, b = b, a + b 
    print()
start = time.time() 
fib(1000)
end = time.time()
print(end - start)

import random 
myList = ["head", "tail"]
while True:
    user = input("Would you like to flip the coin? Yes - y, No - n");
    if user == "Yes" or user == "y":
        coin = random.choice(myList)
        print(coin)
    else:
        break

# practice
three = sum([1 for i in range(1, 101) if i%3 == 0])
print("3의 배수의 개수: ", three)

myList = [("국어", 88), ("수학", 90), ("영어", 99), ("자연", 82)]
print((sorted(myList, key = lambda item : item[1])))

lst = [x for x in range(1, 11)]
print("원래 리스트: ", lst)
even_lst = list(filter(lambda x : x % 2 == 0, lst))
print("짝수 리스트: ", even_lst)
odd_lst = list(filter(lambda x : x % 2 != 0, lst))
print("홀수 리스트: ", odd_lst)

lst = [x for x in range(1, 11)]
print("원래 리스트: ", lst)
f = lambda x : x**3
triple = list(map(f, lst))
print("세제곱된 값: ", triple)

lst = [x for x in range(1, 11)]
print("원래 리스트: ", lst)
f = lambda x : x**2
even = list(map(f, filter(lambda x : x % 2 == 0, lst)))
print("짝수값의 제곱 리스트:", even)

import random 
word_list = ["학습", "컴퓨터", "마우스", "책", "파이썬", "휴대폰", "가방"]
random_list = []
for i in range(3):
    x = random.choice(word_list)
    while x in random_list:
        x = random.choice(word_list)
    random_list.append(x)
print(random_list)

import random 
import string
letter_list = list(string.ascii_lowercase)
letter = []
for i in range(10):
    x = random.choice(letter_list)
    letter.append(x)
print(letter)


def RandomNumber(start, stop, number):
    list = random.sample(range(start, stop + 1), number)
    return list

print(RandomNumber(100, 200, 5))

