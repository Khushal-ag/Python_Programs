file1 = open(r"F:\CODES\Python Programs\File handling\Files\even.txt","w")
file2 = open(r"F:\CODES\Python Programs\File handling\Files\odd.txt","w")

for i in range(1,101):
    if i%2 == 0:
        file1.write(str(i)+" ")
    else:
        file2.write(str(i)+" ")
file1.close()
file2.close()