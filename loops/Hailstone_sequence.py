n = int(input("Enter a number(b/w 50 & 100) = "))
print("Hailstone sequence ->")
while True:
    if n == 1:
        break
    if n%2 == 0:
        n //= 2
    else:
        n = n*3 + 1
    print(n)