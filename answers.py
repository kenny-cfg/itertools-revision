import itertools

def part_02():
    all_integers = itertools.count(0, 1)
    return itertools.islice(all_integers, 10)