import math
a,b,c = map(int,input("Enter three sides -> ").split())
if a+b>c or b+c>a or c+a>b:
    print("VALID")
    if a==b and b==c and c==a:
        print("Equilateral triangle")
    elif (a==b and a==c) or (c==a and c==b) or (b==a and b==c):
        print("Isosceles triangle")
    else:print("Scalene triangle")
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area = ",area)