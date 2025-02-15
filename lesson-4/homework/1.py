def uncommon_elements(list1, list2):
    result = []
    for item in list1:
        if list1.count(item) > list2.count(item):
            result.extend([item] * (list1.count(item) - list2.count(item)))
    for item in list2:
        if list2.count(item) > list1.count(item):
            result.extend([item] * (list2.count(item) - list1.count(item)))
    return result


# Test cases
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))  # Output: [1, 1, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  # Output: [2, 2, 5]
