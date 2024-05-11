def are_lists_equal(list1, list2):
    # Check if the lengths of the lists are equal
    if len(list1) != len(list2):
        return False
    
    # Compare elements of the lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    # If all elements are equal, return True
    return True

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print("Lists:")
print(list1)
print(list2)
print("\nAre the lists equal?", are_lists_equal(list1, list2))
