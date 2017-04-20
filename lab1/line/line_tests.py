import unittest
from line import Line

class LineTests(unittest.TestCase):
   def test_line(self):
      p = Line(1.0,2.0,3.0,4.0)
      self.assertAlmostEqual(p.X1,1.0)
      self.assertAlmostEqual(p.Y1,2.0)
      self.assertAlmostEqual(p.X2,3.0)
      self.assertAlmostEqual(p.Y2,4.0)

      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.

class LineTests2(unittest.TestCase):
   def test_line_again(self):
      g = Line(4.0,3.0,2.0,1.0)
      self.assertAlmostEqual(g.X1,4.0)
      self.assertAlmostEqual(g.Y1,3.0)
      self.assertAlmostEqual(g.X2,2.0)
      self.assertAlmostEqual(g.Y2,1.0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

