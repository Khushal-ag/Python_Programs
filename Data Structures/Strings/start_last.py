s = input("Enter a string = ")
if len(s)<2:
    print("Empty String")
else:
    print("Output =",s[0]+s[1]+s[-2]+s[-1])