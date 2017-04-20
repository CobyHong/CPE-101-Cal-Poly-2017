from utility import *

class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __eq__(self, other):
       xeq = epsilon_equal(self.x, other.x)
       yeq = epsilon_equal(self.y, other.y)
       zeq = epsilon_equal(self.z, other.z)
       return xeq and yeq and zeq

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __eq__(self, other):
     xeq = epsilon_equal(self.x, other.x)
     yeq = epsilon_equal(self.y, other.y)
     zeq = epsilon_equal(self.z, other.z)
     return xeq and yeq and zeq

class Ray:
    def __init__(self,pt,dir):
        self.pt=pt
        self.dir=dir

    def __eq__(self, other):
        pt_eq = (self.pt == other.pt)
        dir_eq = (self.dir == other.dir)
        return pt_eq and dir_eq

class Sphere:
    def __init__(self,center,radius,color):
        self.center=center
        self.radius=radius
        self.color=color

    def __eq__(self, other):
       center_eq = (self.center == other.center)
       radius_eq = epsilon_equal(self.radius, other.radius)
       color_eq = (self.color == other.color)
       return center_eq and radius_eq and color_eq

class Color:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self,other):
        r_eq = epsilon_equal(self.r, other.r)
        g_eq = epsilon_equal(self.g, other.g)
        b_eq = epsilon_equal(self.b, other.b)
        return r_eq and g_eq and b_eq