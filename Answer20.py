fact = 1
for i in range(1, 100):
    fact *= (i+1)
fact = str(fact)


sum = 0
for char in fact:
    sum = sum + int(char)
print(sum)
