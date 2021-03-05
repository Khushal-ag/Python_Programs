n = int(input("Enter a number = "))
if(n<0):
    print("factorial not possible")
elif n==0 or n==1:
    print("Factorial = 1")
else:
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print("Factorial =",fact)