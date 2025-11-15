import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(1), math.pi * 1 * 1)
        self.assertEqual(area(2), math.pi * 2 * 2)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1000000), math.pi * 1000000 * 1000000)

    def test_perimeter(self):
        self.assertEqual(perimeter(1), 2 * math.pi * 1)
        self.assertEqual(perimeter(2), 2 * math.pi * 2)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1000000), 2 * math.pi * 1000000)

    def test_invalid_input(self):
        self.assertEqual(area(-1), 0)
        self.assertEqual(perimeter(-1), 0)
        self.assertEqual(area("sefefere"), 0)
        self.assertEqual(perimeter("egererg"), 0)
