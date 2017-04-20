import unittest
from data import *
import math
from collisions import *

class Test_Assignment_3(unittest.TestCase):

    def test_sphere_intersection_point_1(self):
        ray2 = Ray(Point(0.0,0.0,3.0),Vector(5.0,2.5,1.0))
        sphere2 = Sphere(Point(0.0,5.0,5.0),10.0)
        test2 = sphere_intersection_point(ray2,sphere2)
        self.assertEqual(test2,Point(10.0,5.0,5.0))

    def test_sphere_intersection_point_2(self):
        ray2 = Ray(Point(0.0,-3.0,-3.0),Vector(2.0,1.0,1.0))
        sphere2 = Sphere(Point(0.0,2.0,2.0),10.0)
        test2 = sphere_intersection_point(ray2,sphere2)
        self.assertEqual(test2,Point(10.0,2.0,2.0))

    def test_find_intersection_points_1(self):
        ray2 = Ray(Point(0.0, 0.0, 0.0), Vector(5.0,0.0,0.0))
        sphere1 = Sphere(Point(5.0, 0.0, -5.0), 5.0)
        sphere2 = Sphere(Point(11.0, 0.0, 0.0), 5.0)
        sphere3 = Sphere(Point(17.0, 0.0, 5.0), 5.0)
        sphere_list = [sphere1, sphere2, sphere3]
        test2 = find_intersection_points(sphere_list, ray2)
        self.assertEqual(test2, [(sphere1, Point(5.0, 0.0, 0.0)),
                                           (sphere2, Point(6.0, 0.0, 0.0)),
                                           (sphere3, Point(17.0, 0.0, 0.0))])

    def test_find_intersection_points_2(self):
        ray2 = Ray(Point(0.0, 0.0, 0.0), Vector(2.0, 2.0, 5.0/3.0))
        sphere1 = Sphere(Point(5.0, 0.0, 0.0), 5.0)
        sphere2 = Sphere(Point(11.0, 6.0, 5.0), 5.0)
        sphere3 = Sphere(Point(17.0, 12.0, 10.0), 5.0)
        sphere_list = [sphere1, sphere2, sphere3]
        test2 = find_intersection_points(sphere_list, ray2)
        self.assertEqual(test2, [(sphere1, Point(0.0, 0.0, 0.0)),
                                           (sphere2, Point(6.0, 6.0, 5.0)),
                                           (sphere3, Point(12.0, 12.0, 10.0))])

    def test_sphere_normal_1(self):
        sphere = Sphere(Point(5.0, 0.0, 0.0), 5.0)
        pt = Point(10.0, 0.0, 0.0)
        test1 = sphere_normal_at_point(sphere, pt)
        self.assertEqual(test1, Vector(1.0, 0.0,0.0))

    def test_sphere_normal_2(self):
        sphere = Sphere(Point(5.0, 3.0, 2.0), 3.3)
        pt = Point(1.7, 3.0, 2.0)
        test2 = sphere_normal_at_point(sphere, pt)
        self.assertEqual(test2, Vector(-1.0, 0.0, 0.0))

if __name__ == '__main__':
   unittest.main()