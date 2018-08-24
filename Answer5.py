'''
5. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

"""Answer : Find the primes from 1 to 20, append them to a list, Multiplied the primes from the list.
            Created a method CheckMethod() to check if the number is a number that satisfies the asked condition
            If True function will Return true.
            the gap between checking stage is the multiplication of all the prime numbers between given range,
            because if a number is to be divided by all the numbers that are between the given range,
            it must be multiplied with it's prime numbers in that range.

"""


#Check if number is divis5ible by 1 to 20
from functools import reduce

maxbound = int(input("Enter the maximum number for LCF:"))
prime = []

for num in range(2,maxbound+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        #print(f"Appended {num}")
        prime.append(num)
#print(prime)
#print(len(prime))

mul = reduce(lambda x, y: x*y, prime)

#print(mul)

"""
mul = 1
for i in prime:
    mul *= i

print(mul)
"""

def checkmethod(num):
    for i in range(1,maxbound):
        if num % i !=0:
            return False
    return True

number = mul
while True:
    if checkmethod(number):
        break
    number += mul
print(number)


