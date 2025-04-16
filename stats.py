def count_words(text: str):
    words = text.split()
    word_count = len(words)

    return word_count


def count_characters(text: str):
    character_counts = {}

    for char in text:
        char = char.lower()

        character_counts[char] = character_counts.get(char, 0) + 1

    return character_counts


def sort_criteria(char_dict: dict[str, str | int]):
    return char_dict["count"]


def sort_character_counts(character_counts: dict[str, int]):
    sorted_list = [{"character": char, "count": count} for char, count in character_counts.items()]
    sorted_list.sort(reverse=True, key=sort_criteria)
    return sorted_list
