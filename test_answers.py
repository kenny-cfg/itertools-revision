import unittest

from answers import part_02, part_03, part_04, part_05, part_06, part_07, part_08, part_09, part_10

"""
10. Create a generator that generates the Fibonacci sequence up to the 10th element using `itertools.accumulate`.
11. Use `itertools.compress` to filter elements from a list based on the corresponding boolean values in another list.
12. Write a function that returns the nth element of the Fibonacci sequence using `itertools.islice`.
13. Implement a generator function that generates prime numbers using `itertools.filterfalse`.
14. Use `itertools.takewhile` to generate elements from a list until a condition is met.
15. Write a function that flattens a nested list using `itertools.chain.from_iterable`.
16. Generate all the combinations of 3 elements from the list [1, 2, 3, 4, 5] using `itertools.combinations`.
17. Create a generator that generates the running average of a list using `itertools.accumulate` and `itertools.count`.
18. Use `itertools.groupby` to group the elements of a list by their parity (even or odd).
19. Implement a generator function that generates the powers of 2 using `itertools.count` and `itertools.takewhile`.
20. Use `itertools.dropwhile` to drop elements from a list until a condition is met.
"""


class TestAnswers(unittest.TestCase):
    def test_part_02(self):
        result = part_02()

        self.assertEqual(list(result), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_part_03(self):
        result = part_03([1, 2, 3])

        self.assertEqual(list(result), [1, 2, 3, 1, 2, 3, 1, 2, 3])

    def test_part_04(self):
        result = part_04()

        self.assertEqual(list(result), [5, 5, 5, 5, 5])

    def test_part_05(self):
        result = part_05([1, 2, 3], [4, 5, 6])

        self.assertEqual(list(result), [1, 2, 3, 4, 5, 6])

    def test_part_06(self):
        result = part_06([1, 2, 3], [4], 20)

        self.assertEqual(list(result), [(1, 4), (2, 20), (3, 20)])

    def test_part_07(self):
        result = part_07('abc')

        self.assertEqual(list(result), [('a', 'b', 'c'),
                                        ('a', 'c', 'b'),
                                        ('b', 'a', 'c'),
                                        ('b', 'c', 'a'),
                                        ('c', 'a', 'b'),
                                        ('c', 'b', 'a')])

    def test_part_08(self):
        result = part_08([1, 2, 3, 4])

        self.assertEqual(list(result), [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])

    def test_part_09(self):
        result = part_09([1, 2], ['a', 'b'])

        self.assertEqual(list(result), [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')])

    def test_part_10(self):
        result = part_10()
        # See this:
        # https://github.com/hanif-ali/til/blob/master/python/fibonacci-itertools.md

        self.assertEqual(list(result), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

# 10. Create a generator that generates the Fibonacci sequence up to the
# 10th element using `itertools.accumulate`.

if __name__ == '__main__':
    unittest.main()
