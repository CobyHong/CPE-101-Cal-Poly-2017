import unittest
from data import *

class Test_Assignment_1(unittest.TestCase):
    def test_point_1(self):
        p = Point(1,2,3)
        self.assertEqual(p.x,1)
        self.assertEqual(p.y,2)
        self.assertEqual(p.z,3)

    def test_point_2(self):
        p = Point(3.0,4.0,5.0)
        self.assertAlmostEqual(p.x,3.0)
        self.assertAlmostEqual(p.y,4.0)
        self.assertAlmostEqual(p.z,5.0)

    def test_vector_1(self):
        v = Vector(1,0,1)
        self.assertEqual(v.x,1)
        self.assertEqual(v.y,0)
        self.assertEqual(v.z,1)

    def test_vector_2(self):
        v = Point(5.0,1.0,0.0)
        self.assertAlmostEqual(v.x,5.0)
        self.assertAlmostEqual(v.y,1.0)
        self.assertAlmostEqual(v.z,0.0)

    def test_ray_1(self):
        r = Ray(Point(1,2,3),Vector(1,0,1))
        self.assertEqual(r.pt.x,1)
        self.assertEqual(r.pt.y,2)
        self.assertEqual(r.pt.z,3)
        self.assertEqual(r.dir.x,1)
        self.assertEqual(r.dir.y,0)
        self.assertEqual(r.dir.z,1)

    def test_ray_2(self):
        r = Ray(Point(4.0,5.0,6.0),Vector(5.0,1.0,0.0))
        self.assertAlmostEqual(r.pt.x,4.0)
        self.assertAlmostEqual(r.pt.y,5.0)
        self.assertAlmostEqual(r.pt.z,6.0)
        self.assertAlmostEqual(r.dir.x,5.0)
        self.assertAlmostEqual(r.dir.y,1.0)
        self.assertAlmostEqual(r.dir.z,0.0)

    def test_sphere_1(self):
        s = Sphere(Point(1,2,3),10)
        self.assertEqual(s.center.x,1)
        self.assertEqual(s.center.y,2)
        self.assertEqual(s.center.z,3)
        self.assertEqual(s.radius,10)

    def test_sphere_2(self):
        s = Sphere(Point(4.0,5.0,6.0),20.0)
        self.assertEqual(s.center.x,4.0)
        self.assertEqual(s.center.y,5.0)
        self.assertEqual(s.center.z,6.0)
        self.assertEqual(s.radius,20.0)

if __name__ == '__main__':
   unittest.main()
