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
def armstrong(n):
    l,n1,s = len(str(n)),n,0
    while n1!=0:
        s += pow(n1%10,l)
        n1 //= 10
    if s == n:
        return True
    else:
        return False

s1 = {i for i in range(100,1000) if prime(i) == True}
s2 = {i for i in range(100,1000) if armstrong(i) == True}
print(s1)
print(s2)

#operations
print("Union = ",s1|s2)
print("Intersection = ",s1&s2)
print("Difference = ",s1-s2,s2-s1)
print("Symmetric difference = ",s1^s2)
