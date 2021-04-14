n = int(input("Enter a number = "))
p = 1
while n!=0:
    p *= n
    n -= 1
print("Factorial =",p)