n = int(input("Enter a number = "))
s =0
for i in range(1,n+1):
    if i%2==1:
        s += (i/(i+1))
    else:
        s -= (i / (i + 1))
print("Sum = %.2f"%s)