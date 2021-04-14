n = int(input("Enter a number = "))
c, s = n, 0
while n!=0:
    s = s*10 + n%10
    n //= 10
if s == c:
    print("Pallindrome")
else:
    print("Not Palindrome")
