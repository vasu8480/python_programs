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

