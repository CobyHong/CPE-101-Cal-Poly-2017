from utility import *

class Point:
   def __init__(self,x,y):
       self.x=x
       self.y=y

   def __eq__(self, other):
       xeq = epsilon_equal(self.x, other.x)
       yeq = epsilon_equal(self.y, other.y)
       return xeq and yeq




