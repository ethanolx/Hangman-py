import math

# List methods
def bubble_sort(array, order=None):
    if len(array) != 1:
        i = 0
        cycles_done = 0
        cycles_needed = len(array) - 1
    while cycles_done < cycles_needed:
        while i < (len(array) - 1):
            if array[i] > array[i + 1]:
                smaller = array[i + 1]
                replace_index_list(array, array[i], i + 1)
                replace_index_list(array, smaller, i)
            i += 1
        i = 0
        cycles_done += 1
    if order == 'dsc':
        reverse_list(array)


def replace_index_list(array, new, index):
    array.pop(index)
    array.insert(index, new)


def reverse_list(array):
    length = len(array)
    i = 0
    while i < math.floor(length / 2):
        other = array[length - (i + 1)]
        replace_index_list(array, array[i], (length - (i + 1)))
        replace_index_list(array, other, i)
        i += 1
    return array
