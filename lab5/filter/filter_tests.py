import unittest
from filter import *
from point import *

class TestCases(unittest.TestCase):
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_are_positive_1(self):
        list1 = [-1.4, 4.0, 2.0]
        tpos = are_positive(list1)
        self.assertListAlmostEqual(tpos,[4.0, 2.0])

    def test_are_positive_2(self):
        list2  = [4.0, -4.0, -1.0]
        tpos = are_positive(list2)
        self.assertListAlmostEqual(tpos,[4.0])

    def test_greater_than_1(self):
        list1 = [1.0, 2.0, 3.0]
        tgt = are_greater_than(list1, 4.0)
        self.assertListAlmostEqual(tgt, [])

    def test_greater_than_2(self):
        list2 = [1.0, 2.0, 3.0]
        tgt = are_greater_than(list2, 0.0)
        self.assertListAlmostEqual(tgt, [1.0, 2.0, 3.0])

    def test_first_quadrant_1(self):
        pt1 = Point(-1.0, 3.0)
        pt2 = Point(4.0, 3.0)
        pt3 = Point(0.0, 5.0)
        list1 = [pt1, pt2, pt3]
        tquad1 = are_in_first_quadrant(list1)
        self.assertListAlmostEqual(tquad1, [pt2])

    def test_first_quadrant_2(self):
        pt1 = Point(3.0, 3.0)
        pt2 = Point(4.0, 2.0)
        pt3 = Point(-3.0, -4.0)
        list2 = [pt1, pt2, pt3]
        tquad1 = are_in_first_quadrant(list2)
        self.assertListAlmostEqual(tquad1, [pt1, pt2])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

