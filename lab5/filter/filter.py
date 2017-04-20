import math
import point

def are_positive(list1):
    pos_list = [list1[i] for i in range(len(list1)) if list1[i]>0]
    return pos_list

def are_greater_than(list2,n):
    great_list = []
    for i in range(len(list2)):
        if list2[i]>n:
            great_list.append(list2[i])
    return great_list

def are_in_first_quadrant(list3):
    first_quad = [list3[i] for i in range(len(list3)) if list3[i].x > 0 and list3[i].y > 0]
    return first_quad




