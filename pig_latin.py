# Allow the user enter a message/text

print("Enter a message to be translated to pig latin: ")
text = input()

VOWELS = ('a', 'e', 'i', 'o', 'u')


def pig_latin(message, vowels):
    """Translates the text given into pig latin and prints it."""
    pig_words = []  # A list of words in big latin
    for word in message.split():
        # Separates the non-letters at the start of the words.
        prefix_nonletters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_nonletters += word[0]
            word = word[1:]

        if len(word) == 0:
            pig_words.append(prefix_nonletters)
            continue

        # Separate the non-letters at the end of this word:
        suffix_nonletters = ''
        while not word[-1].isalpha():
            suffix_nonletters += word[-1]
            word = word[:-1]

        # Remember if the word was in uppercase or title case.
        word_upper = word.isupper()
        word_title = word.istitle()

        word = word.lower()  # Makes all the words lowercase for \
        # translation

        # Separate consonants at the start of a word
        prefix_consonants = ''
        while len(word) > 0 and not word[0] in vowels:
            prefix_consonants += word[0]
            word = word[1:]

        # Add the pig latin ending to the word
        if prefix_consonants != '':
            word += f"{prefix_consonants}ay"
        else:
            word += 'yay'

        # Set the word back to uppercase or title case:
        if word_upper:
            word = word.upper()
        if word_title:
            word = word.title()

        # Add the non-letters back to the start or end of the word
        pig_words.append(prefix_nonletters + word + suffix_nonletters)
    # Concatenate all the words back together into a single string:
    print(' '.join(pig_words))


pig_latin(text, VOWELS)
