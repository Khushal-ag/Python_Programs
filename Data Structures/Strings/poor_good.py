s = input("Enter a string = ").split()
s1 = []
if "not" in s:
    if s.index("not") < s.index("poor"):
        for i in range(s.index("not")):
            s1.append(s[i])
        s1 += ["good"]
else:
    s1 = s
print(" ".join(s1))