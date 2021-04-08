# Using only 2 variables
n1 = int(input("Enter first number = "))
n2 = int(input("Enter second number = "))
n1 , n2 = n2 , n1
print("First no.  =" , n1 , "\nSecond no. =" , n2)

# Using 3 variables
n3 = int(input("Enter first number = "))
n4 = int(input("Enter second number = "))
temp = n3
n3 = n4
n4 = temp
print("First no.  =" , n3 , "\nSecond no. =" , n4)