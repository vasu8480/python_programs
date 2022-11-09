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