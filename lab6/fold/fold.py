import point
import math

def sum(list1):
    sum_of_list = 0
    for i in range(len(list1)):
        sum_of_list += list1[i]
    return sum_of_list

def index_of_smallest(list2):
    if len(list2) == 0:
        return -1

    smallest = 0
    for i in range(1,len(list2)): #you said smallest is zero so start checking at 1
        if list2[i] < list2[smallest]: #list2[i] < list2[0]
            smallest = i
    return smallest

def nearest_origin(list3):
    if len(list3) == 0:
        return -1

#Creates new list. Takes Distance of Points in that list. Makes List out of the newfound distance. Returns index of smallest distance.
    dist_list = []
    for i in range(len(list3)):
        dist = math.sqrt((list3[i].x ** 2) + (list3[i].y ** 2))
        dist_list.append(dist)
    return index_of_smallest(dist_list)



