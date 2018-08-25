import time
from math import sqrt, ceil
primeList = []


def isPrime_v1(num):
    if num == 1:
        return False
    else:
        for divisor in range(2, num):
            if num % divisor == 0:
                return False
        return True


def isPrime_v2(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for divisor in range(3, num, 2):
            if num % divisor == 0:
                return False
        return True

def isPrime_v3(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        maxbound = sqrt(num)
        for divisor in range(2, int(maxbound), 2):
            if num % divisor == 0:
                return False
        return True


maxLimit = 1000000
t0 = time.time()
for i in range(1,maxLimit):
    isPrime_v3(i)
    # print(i, isPrime_v1(i))
    # print(i, isPrime_v2(i))
    # print(i, isPrime_v3(i))
t1 = time.time()

print(f"{t1-t0}")


# 01596379280090332
# 54.599947690963745
# 26.080252647399902
