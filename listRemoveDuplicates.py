def remove_duplicates(list_x):
    for item in list_x:
        check = list_x.count(item)
        while check >= 2:
            list_x.remove(item)
            check -= 1
    return sorted(list_x)


def remove_duplicates_set(list_y):
    new_list = set(list_y)
    return list(new_list)


list_of_numbers = [1, 3, 5, 5, 7, 8, 9, 9, 11, 3, 2, 5, 4, 1]
print("\nOriginal list: ", list_of_numbers)
print("* Using for and while loops *")
print("Without duplicates: ", remove_duplicates(list_of_numbers))


list_of_numbers = [1, 3, 5, 5, 7, 8, 9, 9, 11, 3, 2, 5, 4, 1]
print("\n\nOriginal list: ", list_of_numbers)
print("* Using built-in function - 'set' *")
print("Without duplicates: ", remove_duplicates_set(list_of_numbers))
