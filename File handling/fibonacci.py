fp = open(r"F:\CODES\Python Programs\File handling\Files\fibonacci.txt","w")

n = int(input("Enter No. of terms: "))
n1,n2 = 0,1
total = n1 + n2
fp.write(str(n1)+" "+str(n2))
for i in range(n-2):
    fp.write(" "+str(total))
    n1 = n2
    n2 = total
    total = n1 + n2
fp.close()