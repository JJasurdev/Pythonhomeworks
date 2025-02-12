def get_value(dictionary, key, default=None):
    return dictionary.get(key, default)

def check_key(dictionary, key):
    return key in dictionary

def count_keys(dictionary):
    return len(dictionary)

def get_all_keys(dictionary):
    return list(dictionary.keys())

def get_all_values(dictionary):
    return list(dictionary.values())

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def remove_key(dictionary, key):
    dictionary.pop(key, None)

def clear_dictionary():
    return {}

def is_dictionary_empty(dictionary):
    return not bool(dictionary)

def get_key_value_pair(dictionary, key):
    return (key, dictionary[key]) if key in dictionary else None

def update_value(dictionary, key, value):
    dictionary[key] = value

def count_value_occurrences(dictionary, value):
    return sum(1 for v in dictionary.values() if v == value)

def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}

def find_keys_with_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

def check_for_nested_dictionaries(dictionary):
    return any(isinstance(v, dict) for v in dictionary.values())

def get_nested_value(dictionary, *keys):
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return None
    return dictionary

def create_default_dictionary(default_value):
    from collections import defaultdict
    return defaultdict(lambda: default_value)

def count_unique_values(dictionary):
    return len(set(dictionary.values()))

def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))

def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

def filter_by_value(dictionary, condition):
    return {k: v for k, v in dictionary.items() if condition(v)}

def check_for_common_keys(dict1, dict2):
    return bool(set(dict1.keys()) & set(dict2.keys()))

def create_dict_from_tuple(tuples):
    return dict(tuples)

def get_first_key_value_pair(dictionary):
    return next(iter(dictionary.items()), None)
