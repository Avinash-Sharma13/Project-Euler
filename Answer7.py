"""maxbound = int(input())
prime = []

for num in range(2,maxbound+1):
    for i in range(2,num):
        if num % i == 0 or len(prime) == 10001:
            break
    else:
        #print(f"Appended {num}")
        prime.append(num)
#print(prime)
print(len(prime))
"""


def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

print(primes_sieve1(2000000))
