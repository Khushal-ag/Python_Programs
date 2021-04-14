# print sum 1-2+3-4+5......+n

n = int(input("Enter a number = "))
s = 0
for i in range(1,n+1):
    if i%2 == 0:
        s -= i
    else:
        s += i
print("Sum =",s)