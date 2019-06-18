'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

summ = 1000
found = 0
for a in range(1,summ+1):
    for b in range(1,summ+1):
        #print("a =",a,"b =",b)
        c = 1000 - a - b
        if ( (c > 0) and ((a**2+b**2) == c**2) ):
            print("a =",a,"b =",b,"c =",c)
            found = 1
            break
        else:
            pass
    if (found==1):
        break
print("a*b*c =",a*b*c)
