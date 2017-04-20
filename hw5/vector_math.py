import math
from data import *

def scale_vector(vector, scalar):
    a = vector.x * scalar
    b = vector.y * scalar
    c = vector.z * scalar
    return Vector(a,b,c)

def dot_vector(vector1, vector2):
    a = vector1.x * vector2.x
    b = vector1.y * vector2.y
    c = vector1.z * vector2.z
    dot_product = a+b+c
    return dot_product

def length_vector(vector):
    VL = math.sqrt(math.pow(vector.x,2)+math.pow(vector.y,2)+math.pow(vector.z,2))
    return VL

def normalize_vector(vector):
    a = vector.x / length_vector(vector)
    b = vector.y / length_vector(vector)
    c = vector.z / length_vector(vector)
    return Vector(a,b,c)

def difference_point(point1, point2):
    a = point1.x - point2.x
    b = point1.y - point2.y
    c = point1.z - point2.z
    return Vector(a,b,c)

def difference_vector(vector1, vector2):
    a = vector1.x - vector2.x
    b = vector1.y - vector2.y
    c = vector1.z - vector2.z
    return Vector(a,b,c)

def translate_point(point, vector):
    a = point.x + vector.x
    b = point.y + vector.y
    c = point.z + vector.z
    return Point(a,b,c)

def vector_from_to(from_point, to_point):
    a = to_point.x - from_point.x
    b = to_point.y - from_point.y
    c = to_point.z - from_point.z
    return Vector(a,b,c)