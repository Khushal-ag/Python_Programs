fp = open(r"F:\CODES\Python Programs\File handling\Files\armstrong.txt","w")

def armstrong(n):
    n1 = n
    s = 0
    while n1 != 0:
        s += pow(n1%10,len(str(n)))
        n1 //= 10
    if s == n:
        return True
    else:
        return False

for i in range(100,1000):
    if armstrong(i):
        fp.write(str(i)+" ")
fp.close()