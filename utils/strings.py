import math

# String methods
def count_diff_chars(string):
    empty = []
    i = 0
    while i < len(string):
        if string[i] not in empty:
            empty.append(string[i])
        i += 1
    return len(empty)


def find_chars_in_str(string, char):
    numOfLetters = len(string)
    letterIndex = 0
    charIndices = []
    while letterIndex < numOfLetters:
        if string[letterIndex] == char:
            charIndices.append(letterIndex)
        letterIndex += 1
    return charIndices


def insert_index_str(base, additional, index):
    return base[:index] + additional + base[index:]


def remove_index_str(string, index):
    return string[:index] + string[index + 1:]


def replace_index_str(string, new, index):
    return string[:index] + new + string[index + 1:]


def reverse_str(string):
    length = len(string)
    i = 0
    while i < math.floor(length / 2):
        other = string[length - (i + 1)]
        string = replace_index_str(string, string[i], (length - (i + 1)))
        string = replace_index_str(string, other, i)
        i += 1
    return string
