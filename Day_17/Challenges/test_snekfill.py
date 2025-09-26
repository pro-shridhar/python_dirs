import unittest
from the_snake import snakefill  # Make sure this matches your actual file/module name


class TestSnakeFill(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(snakefill(3), 3)

    def test_case_2(self):
        self.assertEqual(snakefill(6), 5)

    def test_case_3(self):
        self.assertEqual(snakefill(24), 9)

    def test_case_4(self):
        self.assertEqual(snakefill(8), 6)

    def test_case_5(self):
        self.assertEqual(snakefill(18), 8)

    def test_case_6(self):
        self.assertEqual(snakefill(555), 18)

    def test_case_7(self):
        self.assertEqual(snakefill(2), 2)

    def test_case_8(self):
        self.assertEqual(snakefill(1), 0)

    def test_case_9(self):
        self.assertEqual(snakefill(900), 19)


if __name__ == "__main__":
    unittest.main()
