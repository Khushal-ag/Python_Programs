#while input("Enter yes or no -> ") == "yes":
age = int(input("Apni age bataye = "))
if age>=7 and age<=100:
    if age<18:
        print("Aap drive nhi krskte")
    elif age==18:
        print("Hm decide nhi krskte physical test dijiye")
    else:
        print("Aap eligible hai")
else:
    print("Shi se daal age")