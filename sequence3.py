'''
Hashtable: 
1) key-value data structure 
2) data structure in which key(index value) of 
the data element is generated from a hash function
3) directly mapping keys to value, much faster
4) data structure efficiently managing wide range of data with little resources
'''

# Structure of dict
# print(__builtins__.__dict__)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1))
# print(hash(t2)) - error raised
# # mutable data type(ex - list) cannot return hash value 

# setdefault() method use
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'), 
          ('k2', 'val4'),
          ('k2', 'val5'))

# Creating tuple source -> dict not using setdefault()

new_dict1 = {}
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)
print(type(new_dict1))

'''

Using setdefault()

What is setdefault()?
Method that returns the value of the item with the specified key
If the key doesn't exist, insert the key:value 

'''
new_dict2 = {}
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print(new_dict2)
x = new_dict2.setdefault('k3', ['val6'])
print(new_dict2)
y = new_dict2.setdefault('k3').append('val7')
# key  = always required, value = optional 
print(new_dict2)