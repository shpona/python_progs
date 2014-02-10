#Program is finding the sum of all the multiples of 3 jr 5 below 1000#
i=1
s=0
while i<1000:
 if i%3==0 or i%5 ==0:
  s=s+i
 i=i+1
print (s)
