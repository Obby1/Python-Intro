words = ['one', 'two', 'three', 'four']

def print_upper_words(words, letters):
    """ collects words and letters and returns words that start
    with letters as uppercase words"""
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print (word.upper())