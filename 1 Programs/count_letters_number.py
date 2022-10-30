str1="vasu is 22"
n,l=0,0
for i in str1:
	if i.isdigit():
		n+=1
	elif i.isalpha():
		l+=1
print(l,n)