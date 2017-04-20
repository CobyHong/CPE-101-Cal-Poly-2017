from data import *
from cast import *
import unittest

class TestCases(unittest.TestCase):
    def test_cast_ray_1(self):
        ray = Ray(Point(0.0, 0.0, 5.0), Vector(0.0, 0.0, -5.0))
        sphere_list = [Sphere(Point(0.0, 0.0, 0.0), 2.0,Color(0.0,  1.0, 1.0), Finish(0.0,0.0))]
        ambient = Color(0.0, 0.0, 0.0)
        light = Light(Point(0,0,100), Color(0.0, 0.0, 0.0))
        casted = cast_ray(ray, sphere_list,ambient,light)
        self.assertEqual(casted, Color(0.0, 0.0, 0.0))

    def test_cast_ray_2(self):
        ray = Ray(Point(0.0, -3.0, -3.0), Vector(2.0, 1.0, 1.0))
        sphere_list = [Sphere(Point(0.0, 2.0, 2.0), 6.0,Color(1.0,  0.0, 0.0), Finish(0.2,0.4))]
        ambient = Color(1.0, 1.0, 0.0)
        light = Light(Point(0,100,100), Color(0.0, 1.0, 0.0))
        casted = cast_ray(ray, sphere_list,ambient,light)
        self.assertEqual(casted, Color(0.2, 0.0, 0.0))

    def test_cast_ray_3(self):
        ray = Ray(Point(0.0, 0.0, 0.0), Vector(5.0, 0.0, 0.0))
        ambient = Color(1.0, 0.0, 1.0)
        light = Light(Point(100,-100,100), Color(1.0,0.0,1.0))
        sphere1 = Sphere(Point(5.0, 0.0, -5.0), 5.0, Color(1.0, 0.0, 0.0), Finish(0.0,0.4))
        sphere2 = Sphere(Point(17.0, 0.0, 5.0), 5.0, Color(0.0, 0.0, 1.0), Finish(0.2,0.4))
        sphere_list = [sphere1, sphere2]
        casted = cast_ray(ray, sphere_list,ambient,light)
        self.assertEqual(casted, Color(0.2347715179942217, 0.0, 0.0))

    def test_cast_ray_4(self):
        ray = Ray(Point(1.0, 2.0, 1.0), Vector(5.0, 7.0, 5.0))
        ambient = Color(1.0, 0.0, 1.0)
        light = Light(Point(100,-100,100), Color(1.0,0.0,1.0))
        sphere1 = Sphere(Point(5.0, 2.0, -10.0), 5.0, Color(1.0, 0.0, 0.0), Finish(0.0,0.4))
        sphere2 = Sphere(Point(13.0, 1.0, 5.0), 5.0, Color(0.0, 0.0, 1.0), Finish(0.2,0.4))
        sphere_list = [sphere1, sphere2]
        casted = cast_ray(ray, sphere_list,ambient,light)
        self.assertEqual(casted, Color(1.0, 1.0, 1.0))

    def test_scaler_1(self):
        check = Color(1.0,2.0,0.5)
        test1 = scaler(check.r)
        test2 = scaler(check.g)
        test3 = scaler(check.b)
        self.assertEqual(test1,255.0)
        self.assertEqual(test2, 255.0)
        self.assertEqual(test3, 127.0)

    def test_scaler_2(self):
        check = Color(6.0,0.0,0.75)
        test1 = scaler(check.r)
        test2 = scaler(check.g)
        test3 = scaler(check.b)
        self.assertEqual(test1,255.0)
        self.assertEqual(test2, 0.0)
        self.assertEqual(test3, 191.0)

if __name__ == '__main__':
   unittest.main()