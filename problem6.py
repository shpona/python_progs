#Program is finding the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
limit=100

def sqr(a): 
	return a*a

summakv=0
summa=0
for i in range (1,limit+1):
	summakv=summakv+sqr(i)
	summa=summa+i
summa=sqr(summa)
raznica=summa-summakv
print(raznica)
