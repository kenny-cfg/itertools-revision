import itertools


def part_02():
    all_integers = itertools.count(0, 1)
    return itertools.islice(all_integers, 10)


def part_03(source: list[int]):
    cycle = itertools.cycle(source)
    return itertools.islice(cycle, 3 * len(source))


def part_04():
    return itertools.repeat(5, 5)


def part_05(first, second):
    return itertools.chain(first, second)


def part_06(first, second, default_value):
    return itertools.zip_longest(first, second, fillvalue=default_value)

def part_07(source):
    return itertools.permutations(source)
