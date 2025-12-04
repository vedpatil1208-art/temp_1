my_list = [1,2,3,2,4,2,5,3,2]
for item in set(my_list):
    print(item, "appears", my_list.count(item), "times")
    