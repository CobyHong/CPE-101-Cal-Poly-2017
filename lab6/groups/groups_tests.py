import unittest
import groups

class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_groups_of_3_1(self):
      list = [1.0,2.0,3.0,4.0,5.0,6.0]
      self.assertListAlmostEqual(groups.groups_of_3(list),[[1.0,2.0,3.0],[4.0,5.0,6.0]])

   def test_groups_of_3_2(self):
       list = [7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
       self.assertListAlmostEqual(groups.groups_of_3(list), [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]])

if __name__ == '__main__':
   unittest.main()
