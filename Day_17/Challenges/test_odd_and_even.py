import unittest
from Day_17.Challenges.sum_of_odd_and_even import sum_odd_and_even


class TestSumOddAndEven(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_odd_and_even([1, 2, 3, 4, 5, 6]), [12, 9])

    def test_negative_numbers(self):
        self.assertEqual(sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])

    def test_zeros_only(self):
        self.assertEqual(sum_odd_and_even([0, 0]), [0, 0])

    def test_empty_list(self):
        self.assertEqual(sum_odd_and_even([]), [0, 0])


if __name__ == "__main__":
    unittest.main()
