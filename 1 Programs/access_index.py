l=[10,23,15,145,65]
for index,val in enumerate(l):
		print(index,val) # 0 10 1 23 2 15 3 145 4 65
#-------------------------------------------
for index,val in enumerate(l,start=1):
		print(index,val) # 1 10 2 23 3 15 4 145 5 65
#-------------------------------------------
for index in range(len(l)):
		print(index,l[index]) # 0 10 1 23 2 15 3 145 4 65
