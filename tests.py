import unittest
from index import sort


class TestPackageSorting(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_bulky_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_bulky_volume(self):
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")


if __name__ == "__main__":
    unittest.main()