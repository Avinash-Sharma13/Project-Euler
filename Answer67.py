tri = []
with open('data/p67.txt', 'r') as f:
    for line in f:
        tri.append([int(x) for x in line.split()])


for _ in range(len(tri)-1):
    for i in range(len(tri)-1):
        tri[-2][i]= tri[-2][i] + max(tri[-1][i], tri[-1][i+1])
    tri.pop()

for char in tri:
    print(char)

