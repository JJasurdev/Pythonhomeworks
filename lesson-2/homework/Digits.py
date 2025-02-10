def check_string_contains_digits():
    user_input = input("Enter a string: ")
    if any(char.isdigit() for char in user_input):
        print("The string contains digits.")
    else:
        print("The string does not contain digits.")

check_string_contains_digits()