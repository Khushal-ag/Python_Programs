import math
def prime(n):
    f = 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            f=0
            break
    if f == 1:
        return True
    else:
        return False

s1 = {i for i in range(1,21) if prime(i) == False}
s2 = {i for i in range(1,11) if i%2 == 0}
print(s1,s2,sep="\n")

#operations
print(s1 >= s2)
print(s2 >= s1)
print(len(s1),len(s2))
print(sum(s1),sum(s2))
