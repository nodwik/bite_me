from itertools import takewhile

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # Erstellen einer Liste von Tupeln (Wort, Wort in Kleinbuchstaben)
    word_tuples = [(word, word.lower()) for word in words]
    # Sortieren nach dem Kleinbuchstaben-Teil des Tupels
    sorted_tuples = sorted(word_tuples, key=lambda x: x[1])
    # Extrahieren der ursprünglichen Wörter aus den sortierten Tupeln
    sorted_words = [word for word, lower_word in sorted_tuples]

    #Wörter, die mit einer Ziffer beginnen
    numb = [nr for nr in takewhile(lambda nr: nr[0].isdigit(), sorted_words)]
    #Wörter, die nicht mit einer Ziffer beginnen
    words_only = [word for word in sorted_words if word not in numb]
    return words_only + numb

words = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()
actual = sort_words_case_insensitively(words)
print(actual)