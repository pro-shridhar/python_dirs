from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passes(self):
        assert True

    def test_always_fails(self):
        assert False


# if __name__ == "__main__":
#     import unittest

#     unittest.main()
