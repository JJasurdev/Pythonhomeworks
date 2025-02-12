def union_of_sets(set1, set2):
    result = set1.copy()
    for elem in set2:
        result.add(elem)
    return result

def intersection_of_sets(set1, set2):
    result = set()
    for elem in set1:
        if elem in set2:
            result.add(elem)
    return result

def difference_of_sets(set1, set2):
    result = set()
    for elem in set1:
        if elem not in set2:
            result.add(elem)
    return result

def check_subset(set1, set2):
    for elem in set1:
        if elem not in set2:
            return False
    return True

def check_element(s, element):
    for elem in s:
        if elem == element:
            return True
    return False

def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def convert_list_to_set(lst):
    result = set()
    for elem in lst:
        result.add(elem)
    return result

def remove_element(s, element):
    if element in s:
        s.remove(element)
    return s

def clear_set(s):
    return set()

def check_if_set_is_empty(s):
    return set_length(s) == 0

def symmetric_difference(set1, set2):
    result = set()
    for elem in set1:
        if elem not in set2:
            result.add(elem)
    for elem in set2:
        if elem not in set1:
            result.add(elem)
    return result

def add_element(s, element):
    s.add(element)
    return s

def pop_element(s):
    if not s:
        return None
    for elem in s:
        s.remove(elem)
        return elem

def find_maximum(s):
    if not s:
        return None
    max_val = None
    for elem in s:
        if max_val is None or elem > max_val:
            max_val = elem
    return max_val

def find_minimum(s):
    if not s:
        return None
    min_val = None
    for elem in s:
        if min_val is None or elem < min_val:
            min_val = elem
    return min_val

def filter_even_numbers(s):
    result = set()
    for elem in s:
        if elem % 2 == 0:
            result.add(elem)
    return result

def filter_odd_numbers(s):
    result = set()
    for elem in s:
        if elem % 2 != 0:
            result.add(elem)
    return result

def create_set_of_range(start, end):
    result = set()
    for i in range(start, end + 1):
        result.add(i)
    return result

def merge_and_deduplicate(lst1, lst2):
    result = set()
    for elem in lst1 + lst2:
        result.add(elem)
    return result

def check_disjoint_sets(set1, set2):
    for elem in set1:
        if elem in set2:
            return False
    return True

def remove_duplicates_from_list(lst):
    result = set()
    for elem in lst:
        result.add(elem)
    return list(result)

def count_unique_elements(lst):
    unique_elements = set()
    for elem in lst:
        unique_elements.add(elem)
    return set_length(unique_elements)

import random

def generate_random_set(size, start, end):
    result = set()
    while set_length(result) < size:
        result.add(random.randint(start, end))
    return result
