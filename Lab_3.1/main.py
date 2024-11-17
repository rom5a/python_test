def search_letters_in_words(letters, words):
    result = []
    word_array = words.split()
    for letter in letters:
        for word in word_array:
            if letter in word:
                result.append(word)
    return result


def open_file(file_name):
    array = []
    with open(file_name) as f:
        for line in f:
            array.append(line)
    return array


words = open_file('words.txt')
letters = 'n'

print (search_letters_in_words(letters, words[0]))