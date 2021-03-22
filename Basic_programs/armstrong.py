n = int(input("Enter a number = "))
n1 = n
c = 0
s = 0
while (n != 0):
    c += 1
    n //= 10
n = n1
while (n != 0):
    s += pow(n%10,c)
    n //= 10
print("Armstrong") if s == n1 else print("Not Armstrong")

