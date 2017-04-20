import data
import cast
import unittest

class TestCases(unittest.TestCase):
    def test_cast_ray_1(self):
        ray = data.Ray(data.Point(0.0, 0.0, 5.0), data.Vector(0.0, 0.0, -5.0))
        sphere_list = [data.Sphere(data.Point(0.0, 0.0, 0.0), 2.0, data.Color(0.0, 1.0, 1.0))]
        casted = cast.cast_ray(ray, sphere_list)
        self.assertEqual(casted, data.Color(0.0, 1.0, 1.0))

    def test_cast_ray_2(self):
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(0.0, 0.0, 1.0))
        sphere_list = []
        casted = cast.cast_ray(ray,sphere_list)
        self.assertEqual(casted, data.Color(1.0,1.0,1.0))

    def test_cast_ray_3(self):
        ray = data.Ray(data.Point(0.0, 0.0, -11.0), data.Vector(0.0, 0.0, 1.0))
        sphere_list = [data.Sphere(data.Point(6.0, 2.0, -3.0), 0.5, data.Color(1.0, 0.0, 0.0))]
        casted = cast.cast_ray(ray,sphere_list)
        self.assertEqual(casted, data.Color(1.0, 1.0, 1.0))

    def test_cast_ray_4(self):
        ray = data.Ray(data.Point(0.0, -3.0, -3.0), data.Vector(2.0, 1.0, 1.0))
        sphere1 = data.Sphere(data.Point(0.0, 2.0, 2.0), 6.0, data.Color(1.0, 0.0, 0.0))
        sphere2 = data.Sphere(data.Point(-10.0, -15.0, -20.0), 2.0, data.Color(0.0, 0.0, 1.0))
        sphere_list = [sphere1, sphere2]
        casted = cast.cast_ray(ray, sphere_list)
        self.assertEqual(casted, data.Color(1.0, 0.0, 0.0))

    def test_cast_ray_5(self):
        ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(5.0, 0.0, 0.0))
        sphere1 = data.Sphere(data.Point(5.0, 0.0, -5.0), 5.0, data.Color(1.0, 0.0, 0.0))
        sphere2 = data.Sphere(data.Point(17.0, 0.0, 5.0), 5.0, data.Color(0.0, 0.0, 1.0))
        sphere_list = [sphere1, sphere2]
        casted = cast.cast_ray(ray, sphere_list)
        self.assertEqual(casted, data.Color(1.0, 0.0, 0.0))


if __name__ == '__main__':
   unittest.main()