def check_palindrome():
    user_input = input("Enter a string: ")
    if user_input == user_input[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

check_palindrome()