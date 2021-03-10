n = int(input("Enter number = "))
if n%3==0 and n%5==0:
    print("TIC-TAC")
elif n%3==0:
    print("TIC")
elif n % 5 == 0:
    print("TAC")