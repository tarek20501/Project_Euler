#Largest prime factor
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number
#600851475143 ?

def isPrime(n):
	if (n==0 or n==1):
		return 0
	if (n==2):
		return 1
	for x in range(2,n):
		if(n%x==0):
			return 0
		else:
			pass
	return 1

def nxtPrime(n):
	while (1):
		n = n+1
		if (isPrime(n)==1):
			return n
		else:
			pass

n = 600851475143
pFac = 2
print(n,"\t",pFac)
while (n!=1):
	if (n%pFac==0):
		n = n//pFac
		print(n,"\t",pFac)
	else:
		pFac = nxtPrime(pFac)
BgstFac = pFac
print()
print(BgstFac)
