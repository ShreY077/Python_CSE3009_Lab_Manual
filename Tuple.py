# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# 1) Add items (Creating a new tuple with added items)
new_tuple = my_tuple + (6, 7)
print("New tuple with added items:", new_tuple)

# 2) len(): Get the length of the tuple
print("Length of the tuple:", len(my_tuple))

# 3) Check for item in tuple
item = 3
if item in my_tuple:
    print(f"{item} is present in the tuple.")
else:
    print(f"{item} is not present in the tuple.")

# 4) Access items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])
