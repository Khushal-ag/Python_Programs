l = [1,5,'hello',1,100,54.7,'hello',5,21,100,78,'ok',54.7,21,10]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)