from itertools import permutations


def possible_permutations(list_of_nums):
    for el in permutations(list_of_nums):
        yield list(el)
