# Tuple unpacking 

# Divmod(a, b) = (a//b, a%b)
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

x, y, *rest = range(10) # Packing
print(x, y, rest)
print(x, y, *(rest)) 
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

# Mutable vs. Immutable

t = (15, 20, 25)
l = [15, 20, 25]

print(id(t))
print(id(l))

t = t * 2
l = l * 2

print(t, id(t))
print(l, id(l))

t *= 2
l *= 2

'''Tuple: keep changing -immutable-> allocating new id
   List: keep changing -mutable-> change reflected on the same list''' 

print(t, id(t))
print(l, id(l)) # List id 'same' 

'''
sort() vs. sorted()

What is the difference? 
sort() func - modifying the list it is called on 
sorted() func - sort newly created list 

When to use?
sort() func - if there's no need to keep the original order of the list 
sorted() func - if it is important to maintain the original order of the list 

'''

# sorted(): reverse, key=len, key=str.lower, key=func...
f_list = ['apple', 'grape', 'banana', 'pineapple', 'orange', 'strawberries']
print('original: ', f_list)
print('sorted: ', sorted(f_list))
print('reverse sorted: ', sorted(f_list, reverse=True))
print('sort based on the length of key:', sorted(f_list, key=len))
print('sort based on the func: ', sorted(f_list, key=lambda x:x[-1]))
print('reverse sort based on the func:', sorted(f_list, key=lambda x:x[-1], reverse=True))

# sort(): reverse, key=len, key=str.lower, key=func...
print('sort: ', f_list.sort(), f_list)
# f_list being modified -> printing 'None'
print('sort: ', f_list.sort(reverse=True), f_list)
print('sort: ', f_list.sort(key=len), f_list)
print('sort: ', f_list.sort(key=lambda x:x[-1]), f_list)
print('sort: ', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)

'''List vs. Array
* list-based: elastic, various data type, wide use 
* array: number-based'''

