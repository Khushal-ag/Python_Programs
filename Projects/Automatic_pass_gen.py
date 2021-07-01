import random as r
import string as s

pass_len = int(input("Enter length of password(min. 4) = "))
dig = list(s.digits)
low = list(s.ascii_lowercase)
upp = list(s.ascii_uppercase)
symbol = list(s.punctuation)
collection = dig + low + upp + symbol
demo_pass = [r.choice(dig), r.choice(low), r.choice(upp), r.choice(symbol)]
demo_pass += r.choices(collection, k=pass_len-4)
r.shuffle(demo_pass)
print("Your Password :","".join(demo_pass))

