def sum_digit(n):
    """This function return sum of digits of entered number"""#dock string
    sum = 0
    while(n!=0):
        sum += n%10
        n //= 10
    return sum
n = int(input("Enetr a number = "))
print(sum_digit.__doc__)#dock string
print("Sum of digit =",sum_digit(n))
