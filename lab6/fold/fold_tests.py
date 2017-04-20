import unittest
import fold
import point

class TestCases(unittest.TestCase):
    def test_sum_1(self):
        list = [1.0,2.0,3.0,4.0,5.0]
        self.assertAlmostEqual(fold.sum(list),15.0)

    def test_sum_2(self):
        list = [6.0,9.0,4.0,2.0,0.0]
        self.assertAlmostEqual(fold.sum(list),21.0)

    def test_index_of_smallest_1(self):
        list = [5.0,2.0,3.0]
        self.assertEqual(fold.index_of_smallest(list),1)

    def test_index_of_smallest_2(self):
        list = [1.0,2.0,3.0]
        self.assertEqual(fold.index_of_smallest(list),0)

    def test_nearest_origin_1(self):
        pt1 = point.Point(1.0,1.0)
        pt2 = point.Point(2.0,2.0)
        list = [pt1,pt2]
        self.assertEqual(fold.nearest_origin(list),0)

    def test_nearest_origin_2(self):
        pt1 = point.Point(6.0,9.0)
        pt2 = point.Point(0.0,0.0)
        list = [pt1,pt2]
        self.assertEqual(fold.nearest_origin(list),1)









# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

