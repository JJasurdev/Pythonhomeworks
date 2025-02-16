import string
from collections import Counter

def create_sample_file():
    with open("sample.txt", "w") as file:
        paragraph = input("Please enter a paragraph to create the sample.txt file:\n")
        file.write(paragraph)

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read().lower()
            return content
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        create_sample_file()
        return read_file(file_name)

def count_words(file_name):
    word_count = Counter()
    
    try:
        with open(file_name, "r") as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = line.split()
                word_count.update(words)
        return word_count
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        create_sample_file()
        return count_words(file_name)

def generate_report(word_count, top_n):
    total_words = sum(word_count.values())
    top_words = word_count.most_common(top_n)

    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'time' if count == 1 else 'times'}")

    # Saving the report to a new file
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report_file.write(f"{word} - {count}\n")

def main():
    top_n = int(input("Enter the number of top common words to display: "))
    content = read_file("sample.txt")
    word_count = count_words("sample.txt")
    generate_report(word_count, top_n)

if __name__ == "__main__":
    main()
