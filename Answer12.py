from math import ceil, sqrt
import time
t0 = time.time()


def divisors(n):
    numberOfFactors = 0
    for i in range(1, int(ceil(sqrt(n)))+1):
        if n % i == 0:
            numberOfFactors += 2
        if i*i == n:
            numberOfFactors -= 1
    return numberOfFactors


# triNum = []
n = 1
nextpos = 1
while True:
    n += 1
    nextpos += n
    # triNum.append(nextpos)
    triNum = nextpos
    cnt = divisors(nextpos)
    if cnt >= 500:
        print(triNum)
        break
t1 = time.time()

print("Time Take : ", t1-t0, "Seconds")
