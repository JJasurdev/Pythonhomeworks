def count_occurrences(lst, element):
    return sum(1 for x in lst if x == element)

def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

def max_element(lst):
    return None if not lst else sorted(lst)[-1]

def min_element(lst):
    return None if not lst else sorted(lst)[0]

def check_element(lst, element):
    return any(x == element for x in lst)

def first_element(lst):
    return None if not lst else lst[0]

def last_element(lst):
    return None if not lst else lst[-1]

def slice_list(lst):
    return lst[:3] if len(lst) >= 3 else lst[:]

def reverse_list(lst):
    return lst[::-1]

def sort_list(lst):
    return sorted(lst)

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def insert_element(lst, index, element):
    lst.insert(index, element)
    return lst

def index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1

def check_for_empty_list(lst):
    return len(lst) == 0

def count_even_numbers(lst):
    return sum(1 for x in lst if x % 2 == 0)

def count_odd_numbers(lst):
    return sum(1 for x in lst if x % 2 != 0)

def concatenate_lists(lst1, lst2):
    return lst1 + lst2

def find_sublist(lst, sublst):
    return any(lst[i:i+len(sublst)] == sublst for i in range(len(lst) - len(sublst) + 1))

def replace_element(lst, old, new):
    return [new if x == old else x for x in lst]

def find_second_largest(lst):
    unique_lst = sorted(set(lst), reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

def find_second_smallest(lst):
    unique_lst = sorted(set(lst))
    return unique_lst[1] if len(unique_lst) > 1 else None

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def list_length(lst):
    return sum(1 for _ in lst)

def create_copy(lst):
    return lst[:]

def get_middle_element(lst):
    n = len(lst)
    return None if n == 0 else (lst[n//2] if n % 2 == 1 else [lst[n//2 - 1], lst[n//2]])

def find_maximum_of_sublist(lst, start, end):
    return None if not lst[start:end] else max(lst[start:end])

def find_minimum_of_sublist(lst, start, end):
    return None if not lst[start:end] else min(lst[start:end])

def remove_element_by_index(lst, index):
    return lst[:index] + lst[index+1:] if 0 <= index < len(lst) else lst

def check_if_list_is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def repeat_elements(lst, times):
    return [x for x in lst for _ in range(times)]

def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def rotate_list(lst, positions):
    return lst[-positions:] + lst[:-positions] if lst else lst

def create_range_list(start, end):
    return list(range(start, end+1))

def sum_of_positive_numbers(lst):
    return sum(x for x in lst if x > 0)

def sum_of_negative_numbers(lst):
    return sum(x for x in lst if x < 0)

def check_palindrome(lst):
    return lst == lst[::-1]

def create_nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def get_unique_elements_in_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
