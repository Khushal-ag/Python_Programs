str1 = input("Enter string to replace: ")
with open(r"F:\CODES\Python Programs\File handling\Files\replace_gla.txt","r") as fp:
    s = fp.read()
    s = s.replace(str1,'GLA')
with open(r"F:\CODES\Python Programs\File handling\Files\b.txt","w") as fp:
    fp.write(s)
