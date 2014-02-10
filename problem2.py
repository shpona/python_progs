#Program is finding the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million#
f1=1
f2=2
fs=0
fs1=0
while f1<4000000:
 if f1%2==0:
  fs1=fs1+f1
 fs=f1+f2 
 f1=f2
 f2=fs
print(fs1)
