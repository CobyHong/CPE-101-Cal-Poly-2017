import unittest
import char

class TestChar(unittest.TestCase):
    def test_lower_1(self):
        string = char.is_lower_101("a")
        self.assertEqual(string,True)

    def test_lower_2(self):
        string = char.is_lower_101("A")
        self.assertEqual(string,False)

    def test_rot_13_1(self):
        string = char.char_rot_13("a")
        self.assertEqual(string,"n")

    def test_rot_13_2(self):
        string = char.char_rot_13("N")
        self.assertEqual(string,"A")

if __name__ == '__main__':
   unittest.main()

