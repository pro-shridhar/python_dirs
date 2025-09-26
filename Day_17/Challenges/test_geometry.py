# test_geometry.py

import unittest
from Day_17.Challenges.geometry_1 import line_length


class TestGeometry(unittest.TestCase):

    def test_diagonal(self):
        self.assertAlmostEqual(line_length([15, 7], [22, 11]), 8.06, places=2)

    def test_same_point(self):
        self.assertAlmostEqual(line_length([0, 0], [0, 0]), 0.00, places=2)

    def test_unit_distance(self):
        self.assertAlmostEqual(line_length([0, 0], [1, 1]), 1.41, places=2)

    def test_negative_coordinates(self):
        self.assertAlmostEqual(line_length([30, 10], [13, -5]), 22.67, places=2)


if __name__ == "__main__":
    unittest.main()
