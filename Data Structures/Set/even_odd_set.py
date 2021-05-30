s1 =  {i for i in range(2,21,2)}
s2 =  {i for i in range(1,20,2)}
print(s1)
print(s2)

#opeartions
print("Union = ",s1|s2)
print("Intersection = ",s1&s2)
print("Difference = ",s1-s2,s2-s1)
print("Symmetric difference = ",s1^s2)
