import unittest
import math
from objects import Point
from objects import Circle
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      p = Point(1,2)
      self.assertEqual(p.x,1)
      self.assertEqual(p.y,2)

   def test_point2(self):
      p1 = Point(3,4)
      self.assertEqual(p1.x,3)
      self.assertEqual(p1.y,4)

   def test_circle(self):
      c = Circle(Point(3,4),2)
      self.assertEqual(c.center.x,3)
      self.assertEqual(c.center.y, 4)
      self.assertEqual(c.radius,2)

   def test_circle2(self):
      c1 = Circle(Point(5,6),3)
      self.assertEqual(c1.center.x,5)
      self.assertEqual(c1.center.y, 6)
      self.assertEqual(c1.radius,3)

   # Add other testing functions
   def distance_function(self):
      p1 = Point(1,2)
      p2 = Point(5,6)
      dist = distance(p1,p2)
      self.assertAlmostEqual(dist,5.6568542)

   def distance_function2(self):
      p1 = Point(1,0)
      p2 = Point(5,0)
      dist = distance(p1,p2)
      self.assertEqual(dist,4)

   def test_circle(self):
      c1 = Circle(Point(3,4),10)
      c2 = Circle(Point(6,8),10)
      overlap = circles_overlap(c1,c2)
      self.assertTrue(overlap)

   def test_circle(self):
      c1 = Circle(Point(3,4),1)
      c2 = Circle(Point(6,8),1)
      overlap = circles_overlap(c1,c2)
      self.assertFalse(overlap)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

