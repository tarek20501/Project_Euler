'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def diff_sum_squares (natural_number):
    sum_of_squares = 0
    for x in range (1,natural_number+1):
        sum_of_squares = sum_of_squares + x**2
    square_of_sum = 0
    for x in range (1,natural_number+1):
        square_of_sum = square_of_sum + x
    square_of_sum = square_of_sum**2
    print(square_of_sum-sum_of_squares)
    return (square_of_sum-sum_of_squares)

diff_sum_squares(100)

#output 25164150