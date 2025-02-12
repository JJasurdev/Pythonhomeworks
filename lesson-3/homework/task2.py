def count_occurrences(tpl, element):
    count = 0
    for x in tpl:
        if x == element:
            count += 1
    return count

def max_element(tpl):
    if not tpl:
        return None
    max_val = tpl[0]
    for x in tpl:
        if x > max_val:
            max_val = x
    return max_val

def min_element(tpl):
    if not tpl:
        return None
    min_val = tpl[0]
    for x in tpl:
        if x < min_val:
            min_val = x
    return min_val

def check_element(tpl, element):
    for x in tpl:
        if x == element:
            return True
    return False

def first_element(tpl):
    return tpl[0] if tpl else None

def last_element(tpl):
    return tpl[-1] if tpl else None

def tuple_length(tpl):
    length = 0
    for _ in tpl:
        length += 1
    return length

def slice_tuple(tpl):
    return tpl[:3] if len(tpl) >= 3 else tpl[:]

def concatenate_tuples(tpl1, tpl2):
    new_tpl = ()
    for x in tpl1:
        new_tpl += (x,)
    for x in tpl2:
        new_tpl += (x,)
    return new_tpl

def check_if_tuple_is_empty(tpl):
    return tuple_length(tpl) == 0

def get_all_indices_of_element(tpl, element):
    indices = []
    for i in range(tuple_length(tpl)):
        if tpl[i] == element:
            indices.append(i)
    return indices

def find_second_largest(tpl):
    unique_elements = list(set(tpl))
    if tuple_length(unique_elements) < 2:
        return None
    first, second = None, None
    for x in unique_elements:
        if first is None or x > first:
            second = first
            first = x
        elif second is None or x > second:
            second = x
    return second

def find_second_smallest(tpl):
    unique_elements = list(set(tpl))
    if tuple_length(unique_elements) < 2:
        return None
    first, second = None, None
    for x in unique_elements:
        if first is None or x < first:
            second = first
            first = x
        elif second is None or x < second:
            second = x
    return second

def create_single_element_tuple(element):
    return (element,)

def convert_list_to_tuple(lst):
    new_tpl = ()
    for x in lst:
        new_tpl += (x,)
    return new_tpl

def check_if_tuple_is_sorted(tpl):
    for i in range(tuple_length(tpl) - 1):
        if tpl[i] > tpl[i + 1]:
            return False
    return True

def find_maximum_of_subtuple(tpl, start, end):
    if start >= end or start < 0 or end > tuple_length(tpl):
        return None
    max_val = tpl[start]
    for i in range(start, end):
        if tpl[i] > max_val:
            max_val = tpl[i]
    return max_val

def find_minimum_of_subtuple(tpl, start, end):
    if start >= end or start < 0 or end > tuple_length(tpl):
        return None
    min_val = tpl[start]
    for i in range(start, end):
        if tpl[i] < min_val:
            min_val = tpl[i]
    return min_val

def remove_element_by_value(tpl, element):
    new_tpl = ()
    removed = False
    for x in tpl:
        if x == element and not removed:
            removed = True
        else:
            new_tpl += (x,)
    return new_tpl

def create_nested_tuple(tpl, size):
    nested_tpl = ()
    for i in range(0, tuple_length(tpl), size):
        nested_tpl += (tpl[i:i+size],)
    return nested_tpl

def repeat_elements(tpl, times):
    repeated_tpl = ()
    for x in tpl:
        repeated_tpl += (x,) * times
    return repeated_tpl

def create_range_tuple(start, end):
    range_tpl = ()
    for i in range(start, end + 1):
        range_tpl += (i,)
    return range_tpl

def reverse_tuple(tpl):
    reversed_tpl = ()
    for i in range(tuple_length(tpl) - 1, -1, -1):
        reversed_tpl += (tpl[i],)
    return reversed_tpl

def check_palindrome(tpl):
    return tpl == reverse_tuple(tpl)

def get_unique_elements(tpl):
    seen = set()
    unique_tpl = ()
    for x in tpl:
        if x not in seen:
            seen.add(x)
            unique_tpl += (x,)
    return unique_tpl
