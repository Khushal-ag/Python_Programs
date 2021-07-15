s = {'Have','a','good','day'}
s1 = s.copy()
for i in s:
    for j in set(i):
        f = 0
        if list(i).count(j) > 1:
            f = 1
            break
    if f == 1:
        s1.remove(i)
print(len(s1))
print(s1)