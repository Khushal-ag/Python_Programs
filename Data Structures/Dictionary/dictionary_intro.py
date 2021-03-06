# dictionary is a key value pair
d1 = {}
print(type(d1))
d2 = {"Khushal": "pasta", "hemant": "kuch nhi", "uv": "paties", "mavendra": {"lunch": "burger", "dinner": "cake"}}
# to add -> d2["ritik"] = "vodka"  or d2.update({"ritik":"vodka"})
del d2["mavendra"]  # delete mavendra
# d3 = d2 # makes a pointer d3 to point d2
d3 = d2.copy()  # makes d3 a copy dictionary of  d2
print(d3)
print(d2.keys())
print(d2.items())
# print(d2["mavendra"]["dinner"])
del d3["uv"]
print(d3, d2)
