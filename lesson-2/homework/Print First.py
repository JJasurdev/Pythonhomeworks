def first_and_last_characters():
    user_input = input("Enter a string: ")
    if user_input:
        print("First character:", user_input[0])
        print("Last character:", user_input[-1])
    else:
        print("The string is empty.")

first_and_last_characters()