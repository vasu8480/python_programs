def ispalindromic (s) :
# Note that s[-jJ for i in [0,len(s) - 1] is st-(i + t)l
	return all(s[i] == s[~i] for i in range(len(s) // 2))
print(ispalindromic("madam"))
#-------------------- Method-2 -----------------------------
str="Madam"
str=str.casefold()
rev=reversed(str)
if (list(str)==list(rev)):
	print('pali')
else:
	print("not pali")
#-------------------- Method-3 -----------------------------
s=""
for i in str:
	s=i+s
if s==str:
	print('pali')
else:
	print("not pali")
#-------------------- Method-4------------------------------
string = list(str)
string.reverse()
print("".join(string))
if s==str:
	print('pali')
else:
	print("not pali")
#-------------------- Method-5 ------------------------------
string = [str[i] for i in range(len(str)-1, -1, -1)]
print("".join(string))
if s==str:
	print('pali')
else:
	print("not pali")