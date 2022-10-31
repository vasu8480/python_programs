#patterns
'''
*
**   
***  
**** 
*****
# '''
for i in range(0,5):
	for j in range(0,i+1):
		print("*",end="")
	print()

myList = []
for i in range(1,5+1):
    myList.append("*"*i)
print("\n".join(myList))

'''
	  *
   **
  ***
 ****
 '''
for row in range(0, 5):
    print(" " * (5 - row) +"*" * row)
		

rows = 5
b = 0
# reverse for loop from 5 to 0
"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
"""
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('')
'''
* * * * *
* * * *
* * *
* *
*
'''
rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")