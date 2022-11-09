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