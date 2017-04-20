import unittest
from map import *
from point import *

class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self,l1,l2):
        self.assertEqual(len(l1),len(l2))
        for el1,el2 in zip(l1,l2):
            self.assertAlmostEqual(el1,el2)

    def square_test_1(self):
        square = square_all([1.0,2.0,3.0,4.0])
        self.assertListAlmostEqual(square,[1.0,4.0,9.0,16.0])

    def square_test_2(self):
        square = square_all([5.0,6.0,7.0,8.0])
        self.assertListAlmostEqual(square,[25.0,36.0,49.0,64.0])

    def add_n_all_test_1(self):
        add_n = add_n_all([1.0,2.0,3.0,4.0],1.0)
        self.assertListAlmostEqual(add_n,[2.0,3.0,4.0,5.0])

    def add_n_all_test_2(self):
        add_n = add_n_all([1.0,2.0,3.0,4.0],2.0)
        self.assertListAlmostEqual(add_n,[3.0,4.0,5.0,6.0])

    def distance_all_test_1(self):
        p1 = Point(3.0,4.0)
        p2 = Point(7.0,24.0)
        p3 = Point(0.0,5.0)
        dist = distane_all([p1,p2,p3])
        self.assertListAlmostEqual(dist,[5.0,25.0,5.0])

    def distance_all_test_2(self):
        p1 = Point(4.0,5.0)
        p2 = Point(5.0,6.0)
        p3 = Point(0.0,3.0)
        dist = distane_all([p1,p2,p3])
        self.assertListAlmostEqual(dist,[6.4,7.81,3.0])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

