import unittest
from Day_17.Challenges.fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(
            fizz_buzz(3), "Fizz", "You gave " + fizz_buzz(3) + " and Fizz was needed"
        )

    def test_buzz(self):
        self.assertEqual(
            fizz_buzz(5), "Buzz", "You gave " + fizz_buzz(5) + " and Buzz was needed"
        )

    def test_fizzbuzz(self):
        self.assertEqual(
            fizz_buzz(15),
            "FizzBuzz",
            "You gave " + fizz_buzz(15) + " and FizzBuzz was needed",
        )

    def test_another_buzz(self):
        self.assertEqual(
            fizz_buzz(10), "Buzz", "You gave " + fizz_buzz(10) + " and Buzz was needed"
        )

    def test_regular_number(self):
        self.assertEqual(
            fizz_buzz(98), "98", "You gave " + fizz_buzz(98) + " and 98 was needed"
        )


if __name__ == "__main__":
    unittest.main()
