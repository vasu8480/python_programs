str="Madam"
str=str.casefold()
rev=reversed(str)
if (list(str)==list(rev)):
	print('pali')
else:
	print("not pali")
#-------------------- Method-2 -----------------------------
s=""
for i in str:
	s=i+s
if s==str:
	print('pali')
else:
	print("not pali")
#-------------------- Method-3------------------------------
string = list(str)
string.reverse()
print("".join(string))
if s==str:
	print('pali')
else:
	print("not pali")
#-------------------- Method-------------------------------
string = [str[i] for i in range(len(str)-1, -1, -1)]
print("".join(string))
if s==str:
	print('pali')
else:
	print("not pali")