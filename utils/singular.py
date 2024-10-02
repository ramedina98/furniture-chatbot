import re
# this function helps me to remove the plural from all the words...
def plural_to_singular_string(str):
    string = str.lower()

    # separate the sentence into words...
    words = string.split()

    # function to convert each plural word into singular word
    def plural_to_singular(word):
        if re.search(r'(ces)$', word):
            # words that end in 'ces
            return re.sub(r'ces$', 'z', word)
        elif re.search(r'([aeiou]s)$', word):
            # words taht end in s...
            return re.sub(r's$', '', word)
        elif re.search(r'(es)$', word) and not re.search(r'([aeiou])es$', word):
            # words taht end in es...
            return re.sub(r'es$', '', word)
        else:
            return word

    singular_words = [plural_to_singular(word) for word in words]

    return ' '.join(singular_words)