import point
import math

def square_all(list1):
    square_list = []
    for i in range(len(list1)):
        square_list.append(list1[i]**2)
    return square_list

def add_n_all(list2,n):
    n_list = [list[i]+n for i in range(len(list2))]
    return n_list

def distance_all(list3):
    dist_list = [ math.sqrt( (list3[i].x**2) + (list3[i].y**2) ) for i in range(len(list3)) ]
    return dist_list

