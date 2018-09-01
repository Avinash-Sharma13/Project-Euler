palindrom = []
import time
start = time.time()
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        mul = j * i
        mul = str(mul)
        if mul == mul[::-1]:
            palindrom.append(int(mul))
            break
print(max(palindrom))
print(time.time() - start)
