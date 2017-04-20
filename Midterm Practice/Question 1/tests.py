import unittest
import triplet

class TestTriplet(unittest.TestCase):

    def test_triplet_1(self):
        list = [0,6,1,2,2,2,5,7]
        test = triplet.reverse_triplet(list)
        self.assertEqual(test, [2, 5])

if __name__ == '__main__':
   unittest.main()
