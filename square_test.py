import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1000000), 1000000 * 1000000)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1000000), 4000000)

    def test_invalid_input(self):
        self.assertEqual(area(-1), 0)
        self.assertEqual(perimeter(-1), 0)
        self.assertEqual(area("jsdfsd"), 0)
        self.assertEqual(perimeter("dsfsdf"), 0)
