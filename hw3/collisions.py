import math
from data import *
from vector_math import *

def sphere_intersection_point(ray, sphere):
    vector_between_point_sphere = difference_point(ray.pt,sphere.center) #VARIABLE

    a = dot_vector(ray.dir,ray.dir)
    b = dot_vector(scale_vector(vector_between_point_sphere,2),ray.dir) #Same as A but first part scales difference_point by 2 (Remember diff point returns vector)
    c = dot_vector(vector_between_point_sphere,vector_between_point_sphere) - (sphere.radius ** 2)
    #Next part uses aspects of Quadratic formula:
    determinant = (b**2) - (4 * a * c) #VARIABLE

    if determinant < 0: #Means there are not roots
        return None
    elif determinant == 0:
        root = (-b)/(2*a) #One root only. Imagine quadratic forumula, where everything in sqrt is 0 so all that is left is -b/2a
        if root >= 0: #Must be positive or cannot use root.
            point = translate_point(ray.pt, scale_vector(ray.dir,root)) #The root is an aspect of t. Scale the ray by the root to find of point of intersection.
            return point
        else:
            return None #If not positive remove.
    if determinant > 0:
        root1 = ( (-b) + math.sqrt(determinant) ) / (2*a)
        root2 = ( (-b) - math.sqrt(determinant) ) / (2*a)

        if (root1 >= 0 and root2 >= 0):
            if root1>root2:
                return translate_point(ray.pt, scale_vector(ray.dir,root2))
            else:
                return translate_point(ray.pt, scale_vector(ray.dir,root1))
        elif root1 > 0 or root2 > 0:
            if root1 > 0:
                return translate_point(ray.pt, scale_vector(ray.dir,root1))
            else:
                return translate_point(ray.pt, scale_vector(ray.dir,root2))

def find_intersection_points(sphere_list, ray):
    ilst = [] #intersection list
    for i in range(len(sphere_list)):
        if (sphere_intersection_point(ray, sphere_list[i]) is not None): #Checks for roots in previous. And if there are roots.
            ilst.append( ( sphere_list[i] , sphere_intersection_point(ray, sphere_list[i]) ) ) #returns object and its intersection. [(Sphere[1],Point),(Sphere[2],Point)]
    return ilst

def sphere_normal_at_point(sphere, point):
    vec_to_pt_sphere = vector_from_to(sphere.center,point)
    return normalize_vector(vec_to_pt_sphere)

