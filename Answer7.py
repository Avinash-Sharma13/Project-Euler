from math import sqrt, floor
import time


def prime(n):
    if n == 1:
            return False  # 1 is not a prime Number
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        maxdivisor = floor(sqrt(n)) + 1
        for divisor in range(3, maxdivisor, 2):
            if n % divisor == 0:
                return False
        return True


t0 = time.time()
n = 1
i = 0
primeatpos = 10001
while True:
    if prime(n):
        i += 1
        # print(n, prime(n))
    if i == primeatpos:
        print(n)
        break
    n += 1
t1 = time.time()

# print(f"Time Taken : {t1 - t0}")
