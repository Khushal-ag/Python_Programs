n = int(input("Enter a number = "))
n1 = n
s = 0
while n != 0:
    s = s*10 + n%10
    n //= 10
if n1 == s:
    print("Pallindrome")
else:
    print("Not Pallindrome")
