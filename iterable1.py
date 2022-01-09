'''
Iterator
- an object that enables to traverse a container 
- iterator type -> uses __iter__ (create an iterator object) 
and __next__ methods (returns the next element in the container)
Generator
- special type of function that returns an iterator object with a sequence of values 
- generator is mostly used in loops to 'generate' an 'iterator' 
'''
# List comprehension
lst1 = [x * x for x in [1, 2, 3, 4, 5, 6, 7]]
print(lst1)
# Generator 
gen1 = (x * x for x in [1, 2, 3, 4, 5, 6, 7])
print(gen1)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))


'''
Iterable types
- collections, text file, sequence types (list, str, tuple), dictionary, set, unpacking, *args...
'''
import string
t = string.ascii_lowercase # __iter__
# print(dir(t))

# Checking iterable type 2

print(hasattr(t, '__iter__'))

# Checking iterable type 3 - inheriting iterable class 
from collections import abc 
print(isinstance(t, abc.Iterable))

# for c in t:
#     print(c)

w = iter(t)
print(dir(w)) #__iter__, __next__

while True:
    try:
        print(next(w))
    except StopIteration:
        break

class WordSplit():
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ') 
    def __next__(self):
        print('Called __next__')
        try: 
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word 
    def __repr__(self):
        return 'WordSplit(%s)'%(self._text)

w = WordSplit("Do not try to be original, just try to be good")
print(w)
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
#print(next(w)) raising error 

class WordSplitGenerator():
    def __init__(self, text):
        self._text = text.split(' ') 
    def __iter__(self):
        for word in self._text:
            yield word 
        return 
    def __repr__(self):
        return 'WordSplitGenerator(%s)' %(self._text)

w = WordSplitGenerator("Do not try to be original, just try to be good")
wt = iter(w)
print(w, wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt)) StopIteration error raised
