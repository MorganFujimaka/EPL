import unittest


def find_repeat(numbers):
    # We do one walk through the list, using a set to keep track of which items we've seen.
    # It gives us O(n) for both time and space.
    numbers_seen = set()

    for num in numbers:
        if num in numbers_seen:
            return num
        numbers_seen.add(num)

    return None


class Test(unittest.TestCase):
    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 95, 67, 1234, 500000, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5, 23, 78, 11, 99, 3891, 758, 2040])
        expected = 4
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
