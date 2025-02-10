def check_string_contains():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    if str2 in str1:
        print(f'"{str2}" is found in "{str1}".')
    else:
        print(f'"{str2}" is not found in "{str1}".')

check_string_contains()