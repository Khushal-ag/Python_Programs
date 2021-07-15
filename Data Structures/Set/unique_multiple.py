set1={4,7,10,5,1}
set2={4,10,2,6,1,9}
x = int(input("Enter a number: "))
tset = set1.union(set2) - set1.intersection(set2)
req_set = set([i for i in tset if i%x==0])
print(req_set)
