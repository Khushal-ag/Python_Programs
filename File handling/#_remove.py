fp1 = open(r"F:\CODES\Python Programs\File handling\Files\remove_content.txt","r")
l = fp1.readlines()
i = 0
while i < len(l):
    if l[i][0] == '#':
        print(l[i],end="")
        l.remove(l[i])
    else:
        i += 1
fp1.close()
with open(r"F:\CODES\Python Programs\File handling\Files\remove_content.txt","w") as fp1:
    fp1.writelines(l)
