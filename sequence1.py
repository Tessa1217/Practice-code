'''Sequence = ordered mutable Set (ex - list)
Python datatype- Container: can contain different types of data (list, tuple, deque)
Python datatype - Flat: solely containing one type (str, bytes, btearray, array, memoryview)
Python datatype - Mutable: (list, bytearray, array, memoryview, deque)
Python datatype - Immutable: (tuple, str, bytes)'''


# List comprehension

chars = '+_)(*&^%$@!'
chars_list = []
for i in chars:
    chars_list.append(ord(i))
print(chars_list)

chars_list2 = [ord(x) for x in chars]
print(chars_list2)

chars_list3 = [ord(x) for x in chars if ord(x) > 40]
print(chars_list3)

chars_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(chars_list4)

# Unicode -> Character
print([chr(s) for s in chars_list])

# List comprehension 2

lst = [['~'] * 3 for i in range(4)]
lst2 = [['~'] * 3] * 4
print(lst)
print(lst2)

lst[0][1] = 'X'
print(lst)
print([id(i) for i in lst])
lst2[0][1] = 'X'
print(lst2)
print([id(i) for i in lst2])

# Generator - iterator 

import array 

tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(array_g.tolist()) # tolist(): Array -> List

# Generator 2 

print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

