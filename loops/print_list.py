list = [1,2,3,"hello",7,8,"hi","bye"]
for i in range(0,len(list)):
    if str(list[i]).isnumeric() and list[i]>6:
        print(list[i])
# Different method
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)
