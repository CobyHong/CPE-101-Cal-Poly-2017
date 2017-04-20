import unittest
import math
from funcs import *

class TestCases(unittest.TestCase):
   def test_f_1(self):
      T1 = f(5)
      self.assertEqual(T1,185)

   def test_f_2(self):
      T2 = f(6)
      self.assertEqual(T2,264)

   def test_f_3(self):
      T3 = g(1,1)
      self.assertEqual(T3,2)

   def test_f_4(self):
      T4 = g(1,2)
      self.assertEqual(T4,5)

   def test_f_5(self):
       T5 = hypotenuse(3,4)
       self.assertEqual(T5,5)

   def test_f_6(self):
       T6 = hypotenuse(5,12)
       self.assertEqual(T6,13)

   def test_f_7(self):
       T7 = is_positive(1)
       self.assertTrue(T7)

   def test_f_8(self):
       T8 = is_positive(-4)
       self.assertFalse(T8)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

