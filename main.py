def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    
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


main()

