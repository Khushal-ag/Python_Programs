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

fp = open(r"F:\CODES\Python Programs\File handling\Files\prime.txt","w")
for i in range(1,101):
    if prime(i):
        fp.write(str(i)+" ")
fp.close()