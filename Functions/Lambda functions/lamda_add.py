from icecream import ic
n1 =  int(input("Enter first no.: "))
n2 =  int(input("Enter second no.: "))

add = (lambda n1,n2:n1+n2)(n1, n2)
ic(add)