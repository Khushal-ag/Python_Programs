a,b = int(input("Enter first number = ")),int(input("Enter second number = "))
s = min(a,b)
l = max(a,b)
gcd = 0
if l%s==0:
    gcd = s
else:
    while (l%s)!=0:
        rem = l%s
        l = s
        s = rem
        gcd = s
lcm = a*b/gcd
print("LCM =",lcm)

