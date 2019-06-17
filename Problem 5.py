#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by
#each of the numbers from 1 to 10 without any 
#remainder.
#What is the smallest positive number that is 
#evenly divisible by all of the numbers from 1 to
#20?

def isDvzbl(n,b,e):
	for x in range(b,e+1):
		if(n%x==0):
			pass
		else:
			return 0
	return 1
	
b = 1
e = 20
n = 1
while (isDvzbl(n,b,e)==0):
	n = n +1
	print(n)
print("\n",n)

#output
#232792560
#1.5e-06
