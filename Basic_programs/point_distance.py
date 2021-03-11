import math
x1,y1 = map(int,input("Enter first point coordinate = ").split())
x2,y2 = map(int,input("Enter second point coordinate = ").split())
d = math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))
print("Distance =",d)