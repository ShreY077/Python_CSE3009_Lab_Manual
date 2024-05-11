# Define a dictionary
my_dict = {'apple': 30, 'banana': 20, 'orange': 25, 'mango': 15}

# Sort the dictionary by values in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort the dictionary by values in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionaries
print("Dictionary sorted by values in ascending order:")
for key, value in sorted_dict_asc.items():
    print(key, ":", value)

print("\nDictionary sorted by values in descending order:")
for key, value in sorted_dict_desc.items():
    print(key, ":", value)
