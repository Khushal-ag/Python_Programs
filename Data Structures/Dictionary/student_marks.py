n,d1,d2 = int(input("Enter no. of records: ")),{},{}
for i in range(n):
    k = input("Enter name: ")
    v = list(map(int,input("Enter marks: ").split()))
    d1[k] = v
print(d1)
for i in d1.keys():
    d2[i] = sum(d1[i])
print(d2)
m = max(d2.values())
for i in d2.keys():
    if d2[i] == m:
        print("Topper: {}\t Marks: {}".format(i,m))
        break