import unittest

from math import pi
import resource

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius > = 0
        self.assertAlmostEqual(resource.circle_area(1), pi)
        self.assertAlmostEqual(resource.circle_area(55), 1)
        self.assertAlmostEqual(resource.circle_area(2.1), pi * 2.1**2)