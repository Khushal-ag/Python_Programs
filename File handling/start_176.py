fp = open(r"F:\CODES\Python Programs\File handling\Files\176_start.txt","r")
l = fp.read().splitlines()
for i in l:
    if i[0:3] == '176':
        print(i)
fp.close()
