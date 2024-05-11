# Create an empty list
my_list = []

# 1) insert(): Insert an element at a specific index
my_list.insert(0, 'a')  # Insert 'a' at index 0
my_list.insert(1, 'b')  # Insert 'b' at index 1
print("After insertions:", my_list)

# 2) remove(): Remove the first occurrence of a value
my_list.remove('a')  # Remove the first occurrence of 'a'
print("After removing 'a':", my_list)

# 3) append(): Append an element to the end of the list
my_list.append('c')  # Append 'c' to the end of the list
print("After appending 'c':", my_list)

# 4) len(): Get the length of the list
print("Length of the list:", len(my_list))

# 5) pop(): Remove and return the last element of the list
last_element = my_list.pop()  # Remove and return 'c'
print("Popped element:", last_element)
print("List after pop:", my_list)

# 6) clear(): Remove all elements from the list
my_list.clear()  # Clear the list
print("List after clearing:", my_list)
