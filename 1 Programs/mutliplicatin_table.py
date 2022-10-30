n=5
for i in range(1,11):
	print(n,'x',i,'=',n*i)
#Multiplication side bye side
for i in range(1,11):
	for j in range(1,11):
		print("{:3d}".format(i*j),end="")
	print()
	