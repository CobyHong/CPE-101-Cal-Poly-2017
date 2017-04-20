from data import *
import math

def sum_function(list1,list2,A):
	if A < len(list2) and a > len(list1):
		return len(list1) + a

list1 = [1,2,10,8]
list2 = ["a","b",10]
a = 50
A = 1
result = sum_function(list1,list2,A)
print(result) #answer be 54 --> len(list1) = 4 + (a=50) --> 4 + 50 = 54

def small(list3):
    smallest = 0
    for i in range(len(list3)):
    	if list3[i] < list3[smallest]:
    		smallest = i
    return list3[smallest]

print(small([3,5,7,1,6,2]))

def swap(string):
    new = ""
    old = string.split(" ")

    for word in old:
        lst = []

        for letter in word:
            lst.append(letter)

        temp1 = lst[0]
        temp2 = lst[-1]
        lst[0] = temp2
        lst[-1] = temp1

        new_word = "".join(lst)
        new += new_word + " "
    return new

def table(a,b):
	if not (a == 5 or b == 5):
		return True
	else:
		return False

print(table(5,5)) #both false = true

def c_in_point(point,circle):
	circle_dist = math.sqrt((point.x-circle.center.x) ** 2 + (point.y-circle.center.y) **2)
	if circle_dist <= circle.radius:
		return True
	else:
		return False

print(c_in_point(Point(10,0),Sphere(Point(0,0),2)))

def filter_nums(list):
	subal = []
	for i in range(len(list)):
		if list[i] <= 8:
			subal.append(i)
	return subal

print(filter_nums([1,2,3,4,5,6,7,8,9,10,11]))





