n = int(input("Enter a number = "))
a, b = 0, 1
print(a,b,end = " ")
for i in range(1,n-1):
    total = a+b
    a = b
    b = total
    print(total,end=" ")
