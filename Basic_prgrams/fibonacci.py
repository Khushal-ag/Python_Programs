n = int(input("Enter a number = "))
a = 0
b = 1
total = 0
for i in range(1, n + 1):
    if n == 1:
        print(a, end="")
        break
    elif n == 2:
        print(a, b, sep="")
        break
    else:
        print(total, end=",")
        a = b
        b = total
        total = a + b
print("\b")