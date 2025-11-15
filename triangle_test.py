import unittest
from triangle import area, perimeter

class FigureTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 3), 6)
        self.assertEqual(area(6, 5), 15)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(1000000, 1000000), 1000000 * 1000000 / 2)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 8), 18)
        self.assertEqual(perimeter(1, 1, 1), 3)
        self.assertEqual(perimeter(1000000, 1000000, 1000000), 3000000)

    def test_invalid_input(self):
        self.assertEqual(area(-1, 4), 0)
        self.assertEqual(perimeter(-1, 4, 5), 0)
        self.assertEqual(area("dfbdbfd", 4), 0)
        self.assertEqual(perimeter("sdfdb", 4, 5), 0)