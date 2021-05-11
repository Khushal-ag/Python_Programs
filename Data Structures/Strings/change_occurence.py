s = input("Enter a string = ")
s1 = s[0]
for i in range(1,len(s)):
    if s[i] == s[0]:
        s1 += "$"
    else:
        s1 += s[i]
print("Output =",s1)