#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of
#two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product
#of two 3-digit numbers.

def isPali(n):
	n = str(n)
	l = 0
	r = len(n)-1
	while (r-l!=1 and r-l!=2):
		if (n[l]==n[r]):
			pass
		else:
			return 0
		l = l+1
		r = r-1
	if(n[l]==n[r]):
		return 1
	else:
		return 0
import os
os.system('cls')
digits = 3
maxPali = 0
for x in range(10**(digits-1),10**(digits)):
	for y in range(10**(digits-1),10**(digits)):
		if(isPali(x*y) and maxPali<(x*y)):
			maxPali = x*y
print(maxPali)