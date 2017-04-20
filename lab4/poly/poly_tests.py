import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_poly(self):
      poly1 = [2.3,4.7,1.0]
      poly2 = [1.2,2.1,-3.2]
      poly3 = poly.poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3,[3.5,6.8,-2.2])

   def test_poly2(self):
      poly1 = [2.4,4.8,2.0]
      poly2 = [1.3,2.2,3.2]
      poly3 = poly.poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3,[3.7,7.0,5.2])

   def test_poly_mult(self):
      poly1 = [1.0,2.0,3.0] # x^2 + 2x + 3
      poly2 = [1.0,3.0,5.0] # x^2 + 3x + 5
      poly3 = poly.poly_mult2(poly1,poly2)
      self.assertListAlmostEqual(poly3,[15.0,19.0,14.0,5.0,1.0]) # 15 + 19x + 14x^2 + 5x^3 + x^4

   def test_poly_mult_2(self):
      poly1 = [3.0,2.0,1.0] # 3x^2 + 2x + 1
      poly2 = [2.0,6.0,4.0] # 2x^2 + 6x + 4
      poly3 = poly.poly_mult2(poly1,poly2)
      self.assertListAlmostEqual(poly3,[4.0,14.0,26.0,22.0,6.0]) # 4 + 14x + 26x^2 + 22x^3 + 6x^4

if __name__ == '__main__':
   unittest.main()
