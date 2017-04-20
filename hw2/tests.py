import unittest
from data import *
from vector_math import *

class Test_Assignment_2(unittest.TestCase):
    def Point_equality_test_1(self):
        a = Point(1.0,2.0,3.0)
        b = Point(1.0,2.0,3.0)
        self.assertEqual(a,b)

    def Point_equality_test_2(self):
        c = Point(5.0,4.0,3.0)
        d = Point(5.0,4.0,3.0)
        self.assertEqual(c,d)

    def Vector_equality_test_1(self):
        a = Vector(1.0,2.0,3.0)
        b = Vector(1.0,2.0,3.0)
        self.assertEqual(a,b)

    def Vector_equality_test_2(self):
        c = Vector(6.0,9.0,6.0)
        d = Vector(6.0,9.0,6.0)
        self.assertEqual(c,d)

    def Ray_equality_test_1(self):
        a = Ray(Point(1.0,2.0,3.0),Vector(4.0,5.0,6.0))
        b = Ray(Point(1.0,2.0,3.0),Vector(4.0,5.0,6.0))
        self.assertEqual(a,b)

    def Ray_equality_test_2(self):
        c = Ray(Point(1.0,1.0,1.0),Vector(1.0,1.0,1.0))
        d = Ray(Point(1.0,1.0,1.0),Vector(1.0,1.0,1.0))
        self.assertEqual(c,d)

    def Sphere_equality_test_1(self):
        a = Sphere(Point(1.0,2.0,3.0),20.0)
        b = Sphere(Point(1.0,2.0,3.0),20.0)
        self.assertEqual(a,b)

    def Sphere_equality_test_1(self):
        c = Sphere(Point(2.0,5.0,1.0),6.0)
        d = Sphere(Point(2.0,5.0,1.0),6.0)
        self.assertEqual(c,d)

    def test_scale_vector(self):
        vc = Vector(1.0,2.0,3.0)
        sv = scale_vector(vc,10)
        self.assertEqual(sv,Vector(10.0,20.0,30.0))

    def test_scale_vector_2(self):
        vc = Vector(4.0,5.0,6.0)
        sv = scale_vector(vc,10)
        self.assertEqual(sv,Vector(40.0,50.0,60.0))

    def test_dot_vector_1(self):
        v1 = Vector(1.0,2.0,3.0)
        v2 = Vector(4.0,5.0,6.0)
        dv = dot_vector(v1,v2)
        self.assertAlmostEqual(dv,32.0)

    def test_dot_vector_2(self):
        v1 = Vector(2.0,3.0,4.0)
        v2 = Vector(5.0,6.0,7.0)
        dv = dot_vector(v1,v2)
        self.assertAlmostEqual(dv,56.0)

    def test_length_vector_1(self):
        v = Vector(1.0,2.0,3.0)
        lv = length_vector(v)
        self.assertAlmostEqual(lv,3.741657387)

    def test_length_vector_2(self):
        v = Vector(4.0,5.0,6.0)
        lv = length_vector(v)
        self.assertAlmostEqual(lv,8.774964387)

    def test_normalize_vector_1(self):
        v = Vector(1.0,2.0,3.0)
        nv = normalize_vector(v)
        self.assertEqual(normalize_vector(v),Vector(0.2672612418962773,0.5345224838248488,0.8017837257372732))

    def test_normalize_vector_2(self):
        v = Vector(4.0,5.0,6.0)
        nv = normalize_vector(v)
        self.assertEqual(normalize_vector(v),Vector(0.4558423058385518,0.5698028822981898,0.6837634587578276))

    def test_difference_point_1(self):
        p1 = Point(1.0,2.0,3.0)
        p2 = Point(4.0,5.0,6.0)
        dp = difference_point(p1,p2)
        self.assertEqual(dp,Vector(-3.0,-3.0,-3.0))

    def test_difference_point_2(self):
        p1 = Point(7.0,8.0,9.0)
        p2 = Point(2.0,1.0,4.0)
        dp = difference_point(p1,p2)
        self.assertEqual(dp,Vector(5.0,7.0,5.0))

    def test_difference_vector_1(self):
        v1 = Vector(10.0,3.0,5.0)
        v2 = Vector(5.0,3.0,2.0)
        dv = difference_vector(v1,v2)
        self.assertEqual(dv,Vector(5.0,0.0,3.0))

    def test_difference_vector_2(self):
        v1 = Vector(11.0,4.0,6.0)
        v2 = Vector(3.0,1.0,8.0)
        dv = difference_vector(v1,v2)
        self.assertEqual(dv,Vector(8.0,3.0,-2.0))

    def test_translate_point_1(self):
        pt = Point(1.0,2.0,3.0)
        vec = Vector(1.0,2.0,3.0)
        tp = translate_point(pt,vec)
        self.assertEqual(tp,Point(2.0,4.0,6.0))

    def test_translate_point_2(self):
        pt = Point(9.0,2.0,3.0)
        vec = Vector(1.0,5.0,6.0)
        tp = translate_point(pt,vec)
        self.assertEqual(tp,Point(10.0,7.0,9.0))

    def test_vector_from_to_1(self):
        to_point = Point(4.0,5.0,6.0)
        from_point = Point(1.0,2.0,3.0)
        vec_from_to = vector_from_to(to_point,from_point)
        self.assertEqual(vec_from_to,Vector(-3.0,-3.0,-3.0))

    def test_vector_from_to_2(self):
        to_point = Point(2.0,3.0,5.0)
        from_point = Point(8.0,9.0,10.0)
        vec_from_to = vector_from_to(to_point,from_point)
        self.assertEqual(vec_from_to,Vector(6.0,6.0,5.0))

if __name__ == '__main__':
   unittest.main()
