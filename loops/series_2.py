# sum of series - 1/2+2/3+3/4+4/5+.....

n = int(input("Enter a number = "))
s = 0
for i in range(1,n+1):
    s += i/(i+1)
print("Sum =",s)