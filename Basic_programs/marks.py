n1 = int(input("Enter marks 1 = "))
n2 = int(input("Enter marks 2 = "))
n3 = int(input("Enter marks 3 = "))
p = (n1 + n2 + n3)/3
if p>=90:
    print("A+")
elif p>=80:
    print("A")
elif p>=70:
    print("B+")
elif p>=60:
    print("B")
else:
    print("Fail")