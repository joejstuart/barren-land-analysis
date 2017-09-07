import unittest
import barrenLand


class BarrenLandTest(unittest.TestCase):

    def test_400_600(self):
        land = barrenLand.fertile_land(600, 400, ['0 292 399 307'])
        self.assertEqual(land, '116800 116800')

    def test_0(self):
        land = barrenLand.fertile_land(3, 2, ['0 0 1 2'])
        self.assertEqual(land, '0')

    def test_smaller_area(self):
        land = barrenLand.fertile_land(5, 6, ['2 0 4 5'])
        self.assertEqual(land, '10 5')

