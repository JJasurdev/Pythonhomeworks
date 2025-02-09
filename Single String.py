def join_words():
    words = input("Enter words separated by spaces: ").split()
    separator = input("Enter a separator (e.g., -, ,): ")
    joined_string = separator.join(words)
    print("Joined string:", joined_string)

join_words()