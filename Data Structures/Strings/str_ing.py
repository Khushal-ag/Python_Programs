s = input("Enter a string = ")
if len(s) >= 3:
    if s[-3:] == "ing":
        s += "ly"
    else:
        s += "ing"
print("Output =",s)