def histo(n):
    for i in range(n):
        print("*",end="")
    print()

s = input("Enter string: ")
d = {}
for i in s:
    d[i] = s.count(i)
for i in d.keys():
    print(i,"\t\t",end="")
    histo(d[i])
