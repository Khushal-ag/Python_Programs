r = int(input("Enter no. of rows: "))
c = int(input("Enter no. of columns: "))
l,d = [],{}
for i in range(r):
    m = []
    for j in range(c):
        e = int(input("Enter [{}][{}] element: ".format(i,j)))
        m.append(e)
    l.append(m)
for i in l:
    print(i)
for i in range(r):
    for j in range(c):
        if l[i][j] != 0:
            d[(i,j)] = l[i][j]
print(d)

