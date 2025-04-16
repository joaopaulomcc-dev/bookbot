import sys

from stats import count_characters, count_words, sort_character_counts


def get_book_text(book_filepath):
    with open(book_filepath, "r") as book_file:
        book_text = book_file.read()

    return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]

    book_text = get_book_text(book_filepath)
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)
    sorted_character_counts_list = sort_character_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}")
    print("----------- Word Count ---------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_data in sorted_character_counts_list:
        if char_data["character"].isalpha():
            print(f"{char_data['character']}: {char_data['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
