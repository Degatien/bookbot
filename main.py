def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = [{"char": char, "count": count} for char, count in chars_dict.items()]

    chars_dict_list.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char_dict in chars_dict_list:
        char = char_dict["char"]
        count = char_dict["count"]
        
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    lowered_text = text.lower()
    chars_dict = {}
    for char in lowered_text:
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1
    return chars_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["count"]
main()

