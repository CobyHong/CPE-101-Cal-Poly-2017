import unittest
from vehicle import Vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
       c = Vehicle(4,100.0,4,True)
       self.assertEqual(c.wheels,4)
       self.assertAlmostEqual(c.fuel,100.0)
       self.assertEqual(c.doors,4)
       self.assertEqual(c.roof,True)

class VehicleTests2(unittest.TestCase):
   def test_vehicle(self):
      s = Vehicle(5, 101.0, 2, False)
      self.assertEqual(s.wheels, 5)
      self.assertAlmostEqual(s.fuel, 101.0)
      self.assertEqual(s.doors, 2)
      self.assertEqual(s.roof, False)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

