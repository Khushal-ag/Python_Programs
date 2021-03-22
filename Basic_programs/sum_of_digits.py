n = int(input("Enter a number = "))
s = 0
while n!=0:
     s += n%10
     n //= 10
print("Sum =",s)