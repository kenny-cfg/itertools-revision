import itertools


def part_02():
    all_integers = itertools.count(0, 1)
    return itertools.islice(all_integers, 10)


def part_03(source: list[int]):
    cycle = itertools.cycle(source)
    return itertools.islice(cycle, 3 * len(source))