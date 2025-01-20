
def word_count(contents :str):
    return len(contents.split())

def count_characters(contents :str):
    characters = {}
    for chr in contents:
        chr = chr.lower()
        if chr not in characters.keys():
            characters[chr] = 0
        characters[chr] += 1
    return characters

def write_report(path :str, word_count :int, character_counts :dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in character_counts.items():
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")

path_to_file = 'books/frankenstein.txt'
with open(path_to_file) as f:
    file_contents = f.read()
    word_count = word_count(file_contents)
    counts = count_characters(file_contents)
    write_report(path_to_file, word_count, counts)
