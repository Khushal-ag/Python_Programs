fp = open(r"F:\CODES\Python Programs\File handling\Files\mean.txt", "r")
s = fp.readline()
c = 1
while s != "":
    s = list(map(int,s.split()))
    sm = sum(s)/len(s)
    print("Mean of {} line is {}".format(c,"%.2f"%sm))
    s = fp.readline()
    c += 1
fp.close()