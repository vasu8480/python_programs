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