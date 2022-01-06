'''
Dict vs. Set
Dict: multiple values per key allowed
Set: not allowed 

'''

# Immutable Dict: read-only dict

from types import MappingProxyType
d = {'k1':'val1'}
d_frozen = MappingProxyType(d)
print(d, id(d))
print(d_frozen, id(d_frozen))

d['k2'] = 'val2'
print(d, id(d)) # Mutable

# d_frozen['k2'] = 'val2'
# print(d_frozen, id(d_frozen))
# Error raised: mappingproxy object is immutable


'''
Set()
'''

# How to create a set?

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Grape'}
print(s1)
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Grape'])
print(s2)
s3 = {'Apple'}
print(s3, type(s3))
s4 = {}
print(s4, type(s4)) # If {} blank, class == 'dict'
s4 = set({})
print(s4, type(s4))

# Frozenset
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Grape'})
print(s5, type(s5)) # class 'frozenset'
# s5.add('Strawberries') -> immutable 

# Comprehending set 

a = {s for s in [1, 2, 3, 4, 5, 5, 5, 6]}
print(a)
a = {s for s in [1, 2, 3, 4, 5, 5, 5, 6] if s%2}
print(a)
a = {s for s in [1, 2, 3, 4, 5, 5, 5, 6] if s%2 == 0}
print(a)
a = {(x, y) for x in range(10) for y in range(10)}
print(a, type(a))

from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)}) # Keyboard 

# Module 'dis': disassembling python bytecode
# Byte code -> Python interpreter runs

from dis import dis
print('-------')
print(dis('{10}'))
print('-------')
print(dis('set([10])'))

