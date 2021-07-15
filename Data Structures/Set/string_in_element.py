s = {'ab','bc','pqr','bcad'}
x = set(input("Enter string: "))
set1 = set([i for i in s if x <= set(i)])
print(set1)
