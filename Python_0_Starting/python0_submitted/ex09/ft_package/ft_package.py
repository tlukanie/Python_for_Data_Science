def count_in_list(lst, word):
    '''Function that counts and returns number of occurrences of
the provided word in the provided list'''
    counter = 0
    for el in lst:
        if el == word:
            counter += 1
    return counter
