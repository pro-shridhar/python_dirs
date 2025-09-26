import unittest
from Imaginary import interview


class TestInterview(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 120), "qualified")

    def test_case_2(self):
        self.assertEqual(interview([2, 3, 8, 6, 5, 12, 10, 18], 120), "qualified")

    def test_case_3(self):
        self.assertEqual(interview([2, 3, 8, 6, 5, 12, 10, 18], 64), "qualified")

    def test_case_4(self):
        self.assertEqual(interview([5, 5, 10, 10, 25, 15, 20, 20], 120), "disqualified")

    def test_case_5(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20], 120), "disqualified")

    def test_case_6(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 130), "disqualified")

    def test_case_7(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 20, 50], 160), "disqualified")

    def test_case_8(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 40], 120), "disqualified")

    def test_case_9(self):
        self.assertEqual(interview([10, 10, 15, 15, 20, 20], 150), "disqualified")

    def test_case_10(self):
        self.assertEqual(interview([5, 5, 10, 20, 15, 15, 20, 20], 140), "disqualified")


if __name__ == "__main__":
    unittest.main()
