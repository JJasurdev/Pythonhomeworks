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

def count_words(content):
    # Remove punctuation and split content into words
    content = content.translate(str.maketrans('', '', string.punctuation))
    words = content.split()
    word_count = Counter(words)
    return word_count

def generate_report(word_count):
    total_words = sum(word_count.values())
    top_5_words = word_count.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} {'time' if count == 1 else 'times'}")

    # Saving the report to a new file
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write("Top 5 Words:\n")
        for word, count in top_5_words:
            report_file.write(f"{word} - {count}\n")

def main():
    content = read_file("sample.txt")
    word_count = count_words(content)
    generate_report(word_count)

if __name__ == "__main__":
    main()

