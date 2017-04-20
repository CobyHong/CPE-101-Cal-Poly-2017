import unittest
import string_101

class TestString(unittest.TestCase):
   def test_string_101_1(self):
      string = string_101.str_rot_13("CobyHong")
      self.assertEqual(string,"PbolUbat")

   def test_string_101_2(self):
      string = string_101.str_rot_13("CoolestCoby")
      self.assertEqual(string,"PbbyrfgPbol")

   def test_str_translate_101_1(self):
       string = string_101.str_translate_101("abcdcba","a","x")
       self.assertEqual(string,"xbcdcbx")

   def test_str_translate_101_2(self):
       string = string_101.str_translate_101("Sax Lover","a","e")
       self.assertEqual(string,"Sex Lover")

if __name__ == '__main__':
   unittest.main()

