s=set([[1,2,3],[3,8,5],[5,7,10],[6,2,0],[5,12,13]])
s1 = set()
for i in range(len(s)-1):
    if sum(s[i]) < sum(s[i+1]):
        s1.update([s[i]])
print(s1)