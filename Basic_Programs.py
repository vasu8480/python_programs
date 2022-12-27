# File: access_index.py
l=[10,23,15,145,65]
for index,val in enumerate(l):
		print(index,val) # 0 10 1 23 2 15 3 145 4 65
#-------------------------------------------
for index,val in enumerate(l,start=1):
		print(index,val) # 1 10 2 23 3 15 4 145 5 65
#-------------------------------------------
for index in range(len(l)):
		print(index,l[index]) # 0 10 1 23 2 15 3 145 4 65

# File: count_each_vowel.py
vowel="aeiou"
str="hello, are you there?"
str=str.casefold()
count={}.fromkeys(vowel,0) # count={'a':0,'e':0,'i':0,'o':0,'u':0}
for char in str:
	if char in count:
		count[char]+=1
print(count) # {'a': 2, 'e': 2, 'i': 0, 'o': 1, 'u': 1}

#------------------------- METHOD 2 -------------------------
str="hello, are you there?".casefold()
count={x:sum([1 for char in str if char==x]) for x in "aeiou"}
print(count) # {'a': 2, 'e': 2, 'i': 0, 'o': 1, 'u': 1}
# File: count_letters_number.py
str1="vasu is 22"
n,l=0,0
for i in str1:
	if i.isdigit():
		n+=1
	elif i.isalpha():
		l+=1
print(l,n)
# File: count_vowels_consonants.py
str1="vasu is a good boy"
v,c=0,0
for i in str1:
	if i=="a" or i=='e'or i=='i' or i=='o' or i=='u':
		v+=1
	else:
		c+=1
print(v,c)
#------------------------ Method-2 ----------------------------------------
a="aeiou"
vo,co=0,0
for char in str1:
	if char in a:
		vo+=1
	else:
		co+=1
print(vo,co)
# File: days_betw_2dates.py
date1="25/10/2022"
date2="25/12/2022"
d1=date1.split("/")
d2=date2.split("/")
diff=(int(d2[0]) + int(d2[1])*30 +int(d2[0])*365)-(int(d1[0]) + int(d1[1])*30 +int(d1[0])*365)
print(diff)
#--------------------------------------- Method-2 --------------------------------------------------------
import calendar
from datetime import datetime
d1=date1.split("/")
d2=date2.split("/")
dat1=calendar.datetime.date(int(d1[2]),int(d1[1]),int(d1[0]))
dat2=calendar.datetime.date(int(d2[2]),int(d2[1]),int(d2[0]))
print((dat2-dat1).days)
# File: fibonacci_series.py
n=6
a=0
b=1
c=0
print(a,b,end=" ")
for i in range(2,n):
	c=a+b
	print(c,end=" ")
	a=b
	b=c
#----------------------------- Method-2 ----------------------------------------
a,b,c=0,1,6
print(a,b,end=" ")
for i in range(2,c):
	d=a+b
	print(d,end=" ")
	a=b
	b=d

# File: Flatten_array.py
#---------------------- only for level-1 flatten ----------------------
l=[[7],[6,5],[1,2,3]]
flat_list=[]
for i in l:
	for val in i:
		flat_list.append(val)
print(flat_list) # [7, 6, 5, 1, 2, 3]
#---------------------- any level flatten ----------------------

flat_list=[]
def flatten(l):
	for i in l:
		if type(i)==list:
			flatten(i)
		else:
			flat_list.append(i)
	return flat_list
l=[[7],[6,[5,[4,5],2]],[1,2,3]]
print(flatten(l)) # [7, 6, 5, 4, 5, 2, 1, 2, 3]

#---------------------- any level flatten ----------------------
def flatten(l):
		if type(l)==list:
			if l==[]:
				return l
			else:
				return flatten(l[0])+flatten(l[1:])
		else:
			return [l]
l=[[7],[6,[5,[4,5],2],[1,2,3]]]
print(flatten(l)) # [7, 6, 5, 4, 5, 2, 1, 2, 3]
# File: gcd.py
n1=21
n2=45
if n1>n2:
	greater=n2
else:
	greater=n1
for i in range(1, greater+1):
    if((n1 % i == 0) and (n2 % i == 0)):
        gcd = i
print( gcd)

#-----------------------------  Method-2 ---------------------------

while n2:
	n1,n2=n2,n1%n2
print(n1)
# File: merge_2_dict.py
dic1={1:'a',2:'b',3:'c'}
dic2={4:'d',5:'e',6:'f'}
print(dic1 |dic2) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
#--------------------- Method2 ----------------
print({**dic1,**dic2}) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
#--------------------- Method3 ----------------
dic1.update(dic2)
print(dic1) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
# File: mutliplicatin_table.py
n=5
for i in range(1,11):
	print(n,'x',i,'=',n*i)
#Multiplication side bye side
for i in range(1,11):
	for j in range(1,11):
		print("{:3d}".format(i*j),end="")
	print()
	
# File: ocurrence_of_a_character.py
str1="vasu is a good a00 boy"
str2="a"
c=0
for i in str1:
	if i==str2:
		c+=1
print(c)
#----------------------------------------------------------------------------------
print(str1.count("a"))
# File: patterns.py
# #patterns
# '''
# *
# **   
# ***  
# **** 
# *****
# # '''
# for i in range(0,5):
# 	for j in range(0,i+1):
# 		print("*",end="")
# 	print()

# myList = []
# for i in range(1,5+1):
#     myList.append("*"*i)
# print(myList)
# print(type(myList))
# print("\n".join(myList))
# print(type("\n".join(myList)))

# '''
# 	  *
#    **
#   ***
#  ****
#  '''
# for row in range(1, 5):
#     print(" " * (5 - row-1) + "*" * row)
		


# # reverse for loop from 5 to 0
# """
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5 
# """


# b = 5
# for i in range(6, 0, -1):
#     b += 1
#     for j in range(0, i ):
#         print(b, end=' ')
#     print()

# '''
# * * * * *
# * * * *
# * * *
# * *
# *
# '''


# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")
# File: sort_alpha_letters.py
my_str="hi i am Vasu" # output: am hi i Vasu
words=[words.lower() for words in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
	print(word,end=" ")

# File: str_pali.py
def ispalindromic (s) :
# Note that s[-jJ for i in [0,len(s) - 1] is st-(i + t)l
	return all(s[i] == s[~i] for i in range(len(s) // 2))
print(ispalindromic("madam"))
#-------------------- Method-2 -----------------------------
str="Madam"
str=str.casefold()
rev=reversed(str)
if (list(str)==list(rev)):
	print('pali')
else:
	print("not pali")
#-------------------- Method-3 -----------------------------
s=""
for i in str:
	s=i+s
if s==str:
	print('pali')
else:
	print("not pali")
#-------------------- Method-4------------------------------
string = list(str)
string.reverse()
print("".join(string))
if s==str:
	print('pali')
else:
	print("not pali")
#-------------------- Method-5 ------------------------------
string = [str[i] for i in range(len(str)-1, -1, -1)]
print("".join(string))
if s==str:
	print('pali')
else:
	print("not pali")
# File: sum_digits_integer.py
n=123
sum=0
while n>0:
	d=n%10
	sum+=d
	n=n//10
print(sum)

num="1456"
su=0
for i in num:
	su+=int(i)

print(su)
# File: sum_of_n_natural_number.py
n=5
sum=0
for i in range(1,n+1):
		sum+=i
print(sum)
# File: swap_number.py
x,y=44,15
x=x+y
y=x-y
x=x-y
print(x,y)
#------------------------------ Method-2----------------------------------------
x=x*y
y=x/y
x=x/y
print(x,y)	#float
#------------------------------ Method-3---------------------------------------
x=x^y
y=x^y
x=x^y
print(x,y)
#------------------------------ Method-4 --------------------------------------------
x,y=y,x
print(x,y)
# File: tempCodeRunnerFile.py
l
# File: w_2dates.py

#---------------------------------Collections-------------------------------------
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

#---------------------------------Itertools-------------------------------------
import itertools as it

a=[1,2]
b=[6,7]

print(list(it.product(a,b))) # [(1, 6), (1, 7), (2, 6), (2, 7)]
print(list(it.product(a,repeat=2))) # [(1, 1), (1, 2), (2, 1), (2, 2)]
print(list(it.product(a,b,repeat=2))) # [(1, 6, 1, 6), (1, 6, 1, 7), (1, 6, 2, 6), (1, 6, 2, 7), (1, 7, 1, 6), (1, 7, 1, 7), (1, 7, 2, 6), (1, 7, 2, 7), (2, 6, 1, 6), (2, 6, 1, 7), (2, 6, 2, 6), (2, 6, 2, 7), (2, 7, 1, 6), (2, 7, 1, 7), (2, 7, 2, 6), (2, 7, 2, 7)]

a=[1,2,3]
#permutations
print(list(it.permutations(a))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(it.permutations(a,2))) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#combinations
#combinations are the subsets of the given list

print(list(it.combinations(a,2))) # [(1, 2), (1, 3), (2, 3)]
print(list(it.combinations_with_replacement(a,2))) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# accumulate
# accumulate() function returns a list containing the accumulated sums.
# accumulate() function takes two parameters, iterable and function.
# If function is not passed, it defaults to addition.
# If function is passed, it should be a function of two arguments that returns a number.
a=[1,2,3]
import operator
print(list(it.accumulate(a))) # [1, 3, 6]
print(list(it.accumulate(a,func=operator.mul))) # [1, 2, 6]
print(list(it.accumulate(a,func=min))) # [1, 1, 1]
print(list(it.accumulate(a,func=max))) # [1, 2, 3]

# groupby
# groupby() function returns a list of tuples where the first element of each tuple is a key and second element is a list of all values corresponding to that key.
# groupby() function takes two parameters, iterable and key.
# If key is not passed, it defaults to None and the element itself is taken as key.
# If key is passed, it should be a function of one argument that returns a key to group by.
# The returned value is an object that applies function to each element to generate the keys for the groupings.
# The object returned by groupby() is not a list, but an iterable object.
# So, we need to iterate over the object to print the grouped data.
# We can use for loop to iterate over the object.
# We can also use list() to convert the iterable object to list.
a=[1,2,3,4]
gb=it.groupby(a,key=lambda x:x<2)
for key,value in gb:
		print(key,list(value)) # True [1] False [2, 3, 4]

a=[1,2,3,4]
gb=it.groupby(a,key=lambda x:x%2)
for key,value in gb:
		print(key,list(value)) # 1 [1, 3] 0 [2, 4]

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
gb=it.groupby(persons,key=lambda x:x['age'])
for key,value in gb:
		print(key,list(value)) # 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}] 27 [{'name': 'Lisa', 'age': 27}] 28 [{'name': 'Claire', 'age': 28}]
 
#count
# count() function returns an iterator that produces consecutive integers.
# count() function takes two parameters, start and step.
# If start is not passed, it defaults to 0.
# If step is not passed, it defaults to 1.
# count() function is an infinite iterator, so we need to use a terminating condition to stop the iteration.

for i in it.count(10,2):
	if i==20:
		break
	print(i) # 10 12 14 16 18

# cycle
# cycle() function returns an iterator that produces elements from the iterable and saves a copy of each.
# When the iterable is exhausted, it returns elements from the saved copy.
# cycle() function takes one parameter, iterable.
# cycle() function is an infinite iterator, so we need to use a terminating condition to stop the iteration.

a=[1,2,3]
for i in it.cycle(a):
	if i==3:
		break
	print(i) # 1 2 3

#repeat
# repeat() function returns an iterator that produces the same value over and over again.
# repeat() function takes two parameters, object and times.
# If times is not passed, it defaults to infinity.
# repeat() function is an infinite iterator, so we need to use a terminating condition to stop the iteration.
a=[1,2,3]
for i in it.repeat(a,2):
	print(i) # [1, 2, 3] [1, 2, 3]

for i in it.repeat(1,2):
	print(i) # 1 1

#takewhile
# takewhile() function returns an iterator yielding elements from the iterable as long as the predicate is true.
# takewhile() function takes two parameters, predicate and iterable.
# If predicate is not passed, it defaults to None.
# If predicate is passed, it should be a function of one argument that returns a boolean value.

a=[1,2,3,4,5]
for i in it.takewhile(lambda x:x<4,a):
	print(i) # 1 2 3

#dropwhile
# dropwhile() function returns an iterator that drops elements from the iterable as long as the predicate is true.
# dropwhile() function takes two parameters, predicate and iterable.
# If predicate is not passed, it defaults to None.
# If predicate is passed, it should be a function of one argument that returns a boolean value.

a=[1,2,3,4,5]
for i in it.dropwhile(lambda x:x<4,a):
	print(i) # 4 5

#filterfalse
# filterfalse() function returns an iterator that filters elements from iterable returning only those for which the predicate is False.
# filterfalse() function takes two parameters, predicate and iterable.
# If predicate is not passed, it defaults to None.
# If predicate is passed, it should be a function of one argument that returns a boolean value.

a=[1,2,3,4,5]
for i in it.filterfalse(lambda x:x<4,a):
	print(i) # 4 5

#compress
# compress() function returns an iterator that filters elements from iterable returning only those that have a corresponding element in selectors that evaluates to True.
# compress() function takes two parameters, iterable and selectors.
# If selectors is not passed, it defaults to None.
# If selectors is passed, it should be a function of one argument that returns a boolean value.

a=[1,2,3,4,5]
for i in it.compress(a,[1,0,1,0,1]):
	print(i) # 1 3 5

#islice
# islice() function returns an iterator that returns selected elements from the iterable.
# islice() function takes three parameters, iterable, start and stop.
# If start is not passed, it defaults to 0.
# If stop is not passed, it defaults to infinity.

a=[1,2,3,4,5]
for i in it.islice(a,2,4):
	print(i) # 3 4

#starmap
# starmap() function returns an iterator that computes the function using arguments obtained from the iterable.
# starmap() function takes two parameters, function and iterable.
# If function is not passed, it defaults to None.
# If function is passed, it should be a function of one argument that returns a boolean value.

a=[(1,2),(3,4),(5,6)]
for i in it.starmap(lambda x,y:x+y,a):
	print(i) # 3 7 11

#tee
# tee() function returns n independent iterators from a single iterable.
# tee() function takes two parameters, iterable and n.
# If n is not passed, it defaults to 2.
# If n is passed, it should be a function of one argument that returns a boolean value.

a=[1,2,3,4,5]
b,c=it.tee(a,2)
for i in b:
	print(i) # 1 2 3 4 5
for i in c:
	print(i) # 1 2 3 4 5

#zip_longest
# zip_longest() function returns an iterator that aggregates elements from each of the iterables.
# zip_longest() function takes two parameters, iterable and fillvalue.
# If fillvalue is not passed, it defaults to None.

a=[1,2,3]
b=[4,5,6,7]
for i in it.zip_longest(a,b,fillvalue=0):
	print(i) # (1, 4) (2, 5) (3, 6) (0, 7)