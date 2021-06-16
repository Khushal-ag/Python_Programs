s = input("Enter string: ")
d = {}
for i in s:
    d[i] = s.count(i)
print(d)
