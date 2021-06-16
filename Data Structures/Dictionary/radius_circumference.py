pi,d,r = 3.14,{},0
print("Enter -1 to exit")
while True:
    r = int(input("Enter radius: "))
    if r == -1:
        break
    else:
        d[r] = round(2*pi*r,2)
print(d)