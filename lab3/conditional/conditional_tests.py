import unittest
from conditional import *

class TestCases(unittest.TestCase):
   def test_case_max_101_1(self):
      max101_1 = max_101(1,2)
      self.assertTrue(max101_1,2)

   def test_case_max_101_2(self):
      max101_2 = max_101(100,2)
      self.assertEqual(max101_2,100)

   def test_case_max_of_three_1(self):
       max3_1 = max_of_three(1,2,3)
       self.assertEqual(max3_1,3)

   def test_case_max_of_three_2(self):
       max3_2 = max_of_three(10,100,50)
       self.assertEqual(max3_2,100)

   def test_case_rental_late_fee_1(self):
       fee_1 = rental_late_fee(0)
       self.assertEqual(fee_1,0)

   def test_case_rental_late_fee_2(self):
       fee_2 = rental_late_fee(3)
       self.assertEqual(fee_2, 5)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

