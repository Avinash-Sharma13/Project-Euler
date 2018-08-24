
sumofsqr = 0

for i in range(1,101):
    sqr = i**2
    sumofsqr +=sqr
    
sumofnums = 0

for i in range(1,101):
    sumofnums += i
sqrofnums = sumofnums**2

print(sqrofnums-sumofsqr)
	
