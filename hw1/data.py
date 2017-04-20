class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class Ray:
    def __init__(self,pt,dir):
        self.pt=pt
        self.dir=dir

class Sphere:
    def __init__(self,center,radius):
        self.center=center
        self.radius=radius

class Color:
    def __init__(self,red,green,blue):
        self.r=red
        self.g=green
        self.b=blue