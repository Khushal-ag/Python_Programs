n =  input("Enter a number = ")
p, s, = len(n), 0
n = int(n)
c = n
while n!=0:
    s += pow(n%10,p)
    n //= 10
if s == c:
    print("Armstrong")
else:
    print("Not Armstrong")




