'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

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

def nthPrime(n):
    i = 0
    j = 0
    while (j < n):
        if (isPrime(i)==1):
            print(str(j+1)+":",end=" ")
            print(i)
            j = j + 1
        i = i + 1
    print("The",n,"th prime number is:",)
    print(i-1)
    return(i-1)

nthPrime(10001)

#output: 104743