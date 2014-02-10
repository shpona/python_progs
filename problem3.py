
#Program is finding the largest prime factor of the number 600851475143#
a=600851475143
i=2
while i<a:
	if a%i==0:
		al=a/i
	else: 
		i+=1
		continue
	n=2
	while n<al:
		if al%n==0:
			break
		n+=1
	if n==al:
		break
	i+=1
print al 
