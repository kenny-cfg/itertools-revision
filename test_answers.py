import unittest

from answers import part_02, part_03

"""
3. Create a cycle that repeats the elements of a list three times.
4. Use `itertools.repeat` to generate a sequence of the number 5 repeated 5 times.
5. Combine two lists using `itertools.chain`.
6. Use `itertools.zip_longest` to combine two lists of different lengths, filling missing values with a default value.
7. Generate all permutations of the characters in the string 'abc'.
8. Generate all combinations of 2 elements from the list [1, 2, 3, 4].
9. Use `itertools.product` to compute the Cartesian product of two lists: [1, 2] and ['a', 'b'].
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



if __name__ == '__main__':
    unittest.main()
