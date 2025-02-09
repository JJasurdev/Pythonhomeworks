def count_vowels_consonants():
    user_input = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in user_input if char in vowels)
    consonant_count = sum(1 for char in user_input if char.isalpha() and char not in vowels)
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

count_vowels_consonants()