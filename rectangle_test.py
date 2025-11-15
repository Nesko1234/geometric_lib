import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 4), 8)
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(0, 4), 0)
        self.assertEqual(area(1000000, 1000000), 1000000 * 1000000)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 4), 12)
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(0, 4), 8)
        self.assertEqual(perimeter(1000000, 1000000), 4000000)

    def test_invalid_input(self):
        self.assertEqual(area(-1, 4), 0)
        self.assertEqual(perimeter(-1, 4), 0)
        self.assertEqual(area("dfvdfvdf", 4), 0)
        self.assertEqual(perimeter("aahahahha", 4), 0)
