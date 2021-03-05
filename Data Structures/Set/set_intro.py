s = set()#main point is it only append unique elements
print(type(s))
l = [1,2,"khushal",5.6]
s=set(l)
print(s)
s.add(5.67)#to add new element
s1 = s.union({1,5,8,"yup"})
s2 = s.intersection({1,5,8,"yup"})
s3 = s.isdisjoint(s1)
#s.remove(value)
print(s,s1,s2,s3)