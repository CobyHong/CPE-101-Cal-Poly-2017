import unittest
import less5

class TestLess5(unittest.TestCase):

    def test_less5_1(self):
        list = ["Jerry","eats","poop","vagina"]
        test = less5.less_than_5(list)
        self.assertEqual(test, 2)

if __name__ == '__main__':
   unittest.main()
