import math
n = int(input("Enter a number = "))
f =0
for i in range(2,int(math.sqrt(n))+1):
     if n%i == 0:
         f = 1
         break
if f==0:
    print("Prime")
else:
    print("Not Prime")
