'''
Pig Latin

Our publishing company has been asked to publish things in Pig Latin for our
customers. We will need a Pig Latin translator that should take in text and
translate it. Pig Latin is a joke variation of english where 2 rules apply:

Words starting with consonants have all leading consonants moved to the end of
the word, and then "ay" is applied:

Words starting with vowels have "way" appended to the end.
Ex: pig -> igpay, arrow -> arrowway
'''

import re

VOWELS = ('a', 'e', 'i', 'o', 'u')


def consonants(word):
    ''' For words beginning with a consonant, shift leading consonants to end
    of word and append "ay" following those consonants.
    '''
    index = 0

    while True:
        if word[index] in VOWELS:
            break

        index += 1

    return '{}{}ay '.format(word[index:], word[:index])


def vowels(word):
    ''' For words beginning with a vowel, append "way" to the end of the input.
    '''
    return '{}way '.format(word)


def format_word(word):
    ''' Remove punctuation and lowercase word, before applying pig latin rules.
    '''
    return re.sub(r'[^\w\s]', '', word).lower()


def pig_latin(word):
    ''' Process each word in the input string, and handle translation
    for words starting with either a vowel or a consonant. Ignore words
    starting with non alphabet characters.
    '''
    translated = ''

    # Apply vowel translation also to words less than 3 chars
    if word[0].lower() in VOWELS or len(word) < 3:
        translated += vowels(word)

    elif word[0].isalpha():
        translated += consonants(word)

    else:
        translated += '{} '.format(word)

    return translated


def translate():
    ''' While user wishes to use translator, accept user input strings to
    translate into pig latin.  Stop execution when user specifies.
    '''

    while True:
        # Collect input string from user for pig latin translation
        input_str = input(
            "Enter the block of text you would like to translate into Pig"
            " Latin:\n"
        )

        pig_latin_str = ""

        # Process translation
        for word in input_str.split():
            pig_latin_str += pig_latin(format_word(word))

        # Return result
        print("The original text entered was: \n'{}'".format(input_str))
        print("The Pig Latin Translation is: \n{}".format(pig_latin_str))

        # See if user wants to test an additional block of text
        cont = input("Would you like to translate additional text? (y/n) ")

        if cont == 'n':
            break


if __name__ == '__main__':
    translate()
