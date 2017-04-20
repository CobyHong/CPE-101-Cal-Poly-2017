import unittest
import convert

class TestConvert(unittest.TestCase):
    def test_convert_1(self):
        string = "BOOB"
        x = 8008
        result = convert.float_default(string,x)
        self.assertEqual(result,8008)

    def test_convert_2(self):
        string = "420"
        x = 9000
        result = convert.float_default(string,x)
        self.assertEqual(result,420)

if __name__ == '__main__':
   unittest.main()

