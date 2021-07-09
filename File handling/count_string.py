s = input("Enter string to count: ")
with open(r"F:\CODES\Python Programs\File handling\Files\count_string.txt","r") as fp:
    data = fp.read().split()
    c = data.count(s)
print("Total occurence:",c)