import math
from objects import Point
from objects import Circle

def distance(a,b):
        dist = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
        return dist

def circles_overlap(circle1,circle2):
        dist = distance(circle1.center, circle2.center) #distance(a,b) placeholders for points(x.y)'s.
        minDistance = (circle1.radius + circle2.radius) #sum - Circle(Point(3,4),10)
        return (dist < minDistance) #If less will return true, meaning they overlap.

