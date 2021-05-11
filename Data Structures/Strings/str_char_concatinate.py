s1 = input("Enter a string 1 = ")
s2 = input("Enter a string 2 = ")
s = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
print("Output =",s)