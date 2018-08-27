num = []
nextpos = 0
triNum = []
i = 0
while True:
    i += 1
    num.append(i)
    nextpos += i
    triNum.append(nextpos)
    divisor = []
    for number in triNum:
        if number % i == 0:
            divisor.append(number)
    print(divisor)
    if len(triNum) == 10:
        break

print(triNum, ":", divisor)

