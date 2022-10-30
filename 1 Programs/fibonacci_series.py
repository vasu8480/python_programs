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
