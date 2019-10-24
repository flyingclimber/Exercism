import string


def is_pangram(sentence):
    letters = string.ascii_lowercase

    for char in sentence.lower():
        letters = letters.replace(char, '')

    if len(letters) == 0:
        return True
    else:
        return False
