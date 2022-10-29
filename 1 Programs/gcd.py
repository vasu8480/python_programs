n1=21
n2=45
if n1>n2:
	greater=n2
else:
	greater=n1
for i in range(1, greater+1):
    if((n1 % i == 0) and (n2 % i == 0)):
        gcd = i
print( gcd)

#-----------------------------  Method-2 ---------------------------

while n2:
	n1,n2=n2,n1%n2
print(n1)