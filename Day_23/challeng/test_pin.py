import unittest
from valid_pin import valid


class TestEmployee(unittest.TestCase):

    def test_valid_pins(self):
        tests = [
            ("123456", True),
            ("4512a5", False),
            ("", False),
            ("21904", False),
            ("9451", True),
            ("213132", True),
            (" 4520", False),
            ("15632 ", False),
            ("000000", True),
        ]

        for pin, expected in tests:
            with self.subTest(pin=pin):
                self.assertEqual(valid(pin), expected)
