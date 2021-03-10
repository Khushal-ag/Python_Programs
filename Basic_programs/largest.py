n1 = int(input("Enter first number = "))
n2 = int(input("Enter second number = "))
n3 = int(input("Enter third number = "))
if n1>n2:
    if n1>n3:
        print("{} is largest".format(n1))
    else:
        print("{} is largest".format(n3))
else:
    if n2>n3:
        print("{} is largest".format(n2))
    else:
        print("{} is largest".format(n3))