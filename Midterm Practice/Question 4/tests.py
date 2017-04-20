import unittest
import listlist

class TestLess5(unittest.TestCase):

    def test_listlist_1(self):
        list = [ [1, 2, 3] , [4, 5, 6] , [7 , 8, 9] ]
        test = listlist.diagnol(list)
        self.assertEqual(test, [1 ,5 ,9])

if __name__ == '__main__':
   unittest.main()
