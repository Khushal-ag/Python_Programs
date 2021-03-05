#Faulty calculator
n1 = int(input("Enter first operant = "))
n2 = int(input("Enter second operant = "))
o = input("Enter operator you want to apply = ")
if o=='+':
    if n1==56 and n2==9:
        ans = 77
    else:
        ans = n1 + n2
elif o == '*':
    if n1 == 45 and n2 == 3:
        ans = 555
    else:
        ans = n1 * n2
elif o=='/':
    if n1==56 and n2==6:
        ans = 4
    else:
        ans = n1 / n2
elif o=='-':
    ans = n1 - n2
elif o=='%':
    ans = n1 % n2
print("Answer =",ans)