a,b = int(input("Enter first number = ")),int(input("Enter second number = "))
s = min(a,b)
l = max(a,b)
c = 1
if l%s==0:
    print("GCD =",s,"\nSteps Taken =",c+1)
else:
    while (l%s)!=0:
        c += 1
        rem = l%s
        l = s
        s = rem
    print("GCD =",s)
    print("Steps Taken =",c)

