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