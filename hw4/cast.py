from data import *
from vector_math import *
from collisions import *

def cast_ray(ray,sphere_list):
    c = find_intersection_points(sphere_list,ray)
    if c == []:
        return Color(1.0,1.0,1.0)
    else:
        nearest = 0
        for i in range(len(c)):
            if length_vector(vector_from_to(ray.pt,c[i][1])) < length_vector(vector_from_to(ray.pt,c[nearest][1])): #[i][i of tuple]
                nearest = i
        return c[nearest][0].color #return sphere part, color part.

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    w_interval = (max_x - min_x)/float(width)
    h_interval = (max_y - min_y)/float(height)

    for i2 in range(height):
        y = max_y - (i2 * h_interval)
        for i in range(width):
            x = min_x + (i * w_interval)

            dir = vector_from_to(eye_point,Point(x,y,0))
            ray = Ray(eye_point,dir)
            check = cast_ray(ray,sphere_list)

            r = scaler(check.r)
            print(r)

            g = scaler(check.g)
            print(g)

            b = scaler(check.b)
            print(b)

def scaler(check):
    result = int(check * 255)
    if result > 255:
        result = 255
    return result