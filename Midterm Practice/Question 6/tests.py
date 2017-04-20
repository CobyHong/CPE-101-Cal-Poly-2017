import unittest
import slicing

class TestSlicing(unittest.TestCase):

    def test_change_1(self):
        string = "Pen15"
        test = change.change_nums_only(string)
        self.assertEqual(test, "Pen37")

if __name__ == '__main__':
   unittest.main()
