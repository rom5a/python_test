def search_letters_in_words(letters, words):
    result = []
    word_array = words.split()
    for letter in letters:
        for word in word_array:
            if letter in word:
                result.append(word)
    return result


letters = 'n'
words = 'asas dsad nnnn asdn snna'

print (search_letters_in_words(letters, words))