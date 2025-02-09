def count_words_in_sentence():
    sentence = input("Enter a sentence: ")
    word_count = len(sentence.split())
    print("Number of words:", word_count)

count_words_in_sentence()