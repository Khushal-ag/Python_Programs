n,d1,d2 = int(input("Enter key-pairs to be enter: ")),{},{}
for i in range(n):
    k = eval(input("Enter key: "))
    v = input("Enter value: ")
    d1[k] = v
print(d1)
for i in d1.keys():
    d2[d1[i]] = i
print(d2)