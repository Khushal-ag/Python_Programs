import math
a,b,c = map(int,input("Enter a b c -> ").split())
d = pow(b,2) - 4*a*c
if d>=0:
    if d==0:
        print("Roots are real and equal")
    else:
        print("Roots are real and unequal")
else:
    print("Roots are imaginary")
r1 = (-b + math.sqrt(d))/(2*a)
r2 = (-b - math.sqrt(d))/(2*a)
print("Root 1 -> {}\nRoot 2 -> {}".format(r1,r2))