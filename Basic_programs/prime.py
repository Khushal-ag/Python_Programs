import math
n = int(input("Enter a number = "))
f,i,c = 0,2,0
while i<=math.sqrt(n):
    c += 1
    if n%i==0:
        f = 1
        break
    i += 1
if f==0:
    print("Prime")
else:
    print("Not Prime")
print("Steps Taken =",c)