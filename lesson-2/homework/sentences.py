def replace_word_in_sentence():
    sentence = input("Input sentence: ")
    word_to_replace = input("Replace: ")
    new_word = input("With: ")
    new_sentence = sentence.replace(word_to_replace, new_word)
    print("Output:", new_sentence)

replace_word_in_sentence()
