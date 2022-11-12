import collections as c
a="abbcscs"

print(c.Counter(a)) # Counter({'b': 2, 'c': 2, 'a': 1, 's': 1})
print(c.Counter(a).items()) # dict_items([('a', 1), ('b', 2), ('c', 2), ('s', 1)])
print(c.Counter(a).keys()) # dict_keys(['a', 'b', 'c', 's'])
print(c.Counter(a).values()) # dict_values([1, 2, 2, 1])

#most_common() returns a list of tuples with the most common elements and their counts in the order of most common to least common.

print(c.Counter(a).most_common(2)) # [('b', 2), ('c', 2)]
print(c.Counter(a).most_common(2)[0]) # ('b', 2)
print(c.Counter(a).most_common(2)[0][0]) # b
print(c.Counter(a).most_common(2)[0][1]) # 2

print(c.Counter(a).most_common(1)) # [('b', 2)]
print(c.Counter(a).most_common(1)[0][0]) # b

print(list(c.Counter(a).elements())) # ['a', 'b', 'b', 'c', 'c', 's']

#ordereddict is a dictionary subclass that remembers the order that keys were first inserted.
#The only difference between dict() and OrderedDict() is that: OrderedDict() remembers the order in which the keys were inserted.
#A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order.

ord={}
ord['a']=1
ord['b']=2
ord['c']=3
ord['d']=4
ord['e']=5
print(ord) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

#defaultdict is a dictionary subclass that calls a factory function to supply missing values.
#defaultdict is a dictionary-like object which provides all methods provided by dictionary but takes first argument (default_factory) as default data type for the dictionary.
#Using defaultdict is faster than doing the same using dict.set_default method.

d=c.defaultdict(int) 
d['a']=1
d['b']=2
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a']) # 1
print(d['c']) # 0 #default value of int is 0 so it returns 0 if key is not present


#deque is a list-like container with fast appends and pops on either end.
#deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
dec=c.deque()
dec.append(1)
dec.append(2)
dec.append(3)
print(dec) # deque([1, 2, 3])
dec.appendleft(4)
print(dec) # deque([4, 1, 2, 3])
dec.pop()
print(dec) # deque([4, 1, 2])
dec.popleft()
print(dec) # deque([1, 2])
dec.extend([7,8,9])
print(dec) # deque([1, 2, 7, 8, 9])
dec.extendleft([10,11,12])
print(dec) # deque([12, 11, 10, 1, 2, 7, 8, 9])
dec.rotate(1)
print(dec) # deque([9, 12, 11, 10, 1, 2, 7, 8])
dec.rotate(2)
print(dec) # deque([7, 8, 9, 12, 11, 10, 1, 2])
dec.rotate(-1)
print(dec) # deque([12, 11, 10, 1, 2, 7, 8, 9])

#namedtuple returns a tuple object with names for each position of the tuple.
#namedtuple() function is a factory function that returns a subclass of tuple with named fields.
#namedtuple() is used to create tuple subclasses with named fields.
#namedtuple() is a factory function that returns a subclass of the standard Python tuple type.
#namedtuple() is used to create tuple subclasses with named fields.
#namedtuple() is a factory function that returns a subclass of the standard Python tuple type.

Point=c.namedtuple('Point',['x','y'])
p=Point(11,y=22)
print(p[0]+p[1]) # 33
print(p.x+p.y) # 33
x,y=p
print(x,y) # 11 22
print(p) # Point(x=11, y=22)

