s = input("Enter string: ").split()
d = {}
for i in s:
    d[i] = s.count(i)
print(d)
