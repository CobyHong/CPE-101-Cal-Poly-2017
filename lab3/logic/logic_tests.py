import unittest
from logic import *

class TestCases(unittest.TestCase):
   def test_case_test_is_even_1(self):
      Even_1 = is_even(6)
      self.assertTrue(Even_1)

   def test_case_test_is_even_2(self):
      Even_2 = is_even(5)
      self.assertFalse(Even_2)

   def test_cases_in_an_interval_1(self):
       Interval_1 = in_an_interval(50)
       self.assertTrue(Interval_1)

   def test_cases_in_an_interval_2(self):
       Interval_2 = in_an_interval(21)
       self.assertFalse(Interval_2)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

