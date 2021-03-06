amount = int(input("Enter amount = "))
n2000 = amount//2000
amount %= 2000
n500 = amount//500
amount %= 500
n100 = amount//100
print("2000 notes =",n2000)
print("500 notes =",n500)
print("100 notes =",n100)
