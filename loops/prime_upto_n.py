import math
n = int(input("Enter a number = "))
print("Prime no. -> ",end="")
for k in range(1,n+1):
    f =0
    for i in range(2,int(math.sqrt(k))+1):
         if k%i == 0:
             f = 1
             break
    if f==0:
        print(k,end=" ")
  