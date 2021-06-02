s1 = {i ** 2 for i in range(1,11)}
s2 = {i ** 3 for i in range(1,11)}
print(s1,s2,sep="\n")

#operations

s1.update(s2)
print(s1)
print("pop element = ",s1.pop())
s1.remove(4)
print(s1)
s1.add(4)
print(s1)
s1.clear()
print(s1)