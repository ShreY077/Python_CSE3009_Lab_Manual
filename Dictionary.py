# Create a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# 1) Print the dictionary items
print("Dictionary items:")
for key, value in my_dict.items():
    print(key, ":", value)

# 2) Access items
print("\nAccess items:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# 3) Use get()
print("\nUse get():")
print("Name:", my_dict.get('name'))
print("Country:", my_dict.get('country', 'Not found'))

# 4) Change values
print("\nChange values:")
my_dict['age'] = 35
print("Updated age:", my_dict['age'])

# 5) Use len()
print("\nLength of the dictionary:", len(my_dict))
