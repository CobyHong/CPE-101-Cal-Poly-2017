import data
import vector_math
import collisions


def cast_ray(ray,sphere_list):
    c = collisions.find_intersection_points(sphere_list, ray)
    if len(c) > 0:
        closest = c[0]  # Sphere0 , Point (x,y,z)
                        #   x[0]        x[1]
        for x in c:
            if vector_math.length_vector(c.ray.pt,x[1]) < vector_math.length_vector(c.ray.pt,closest[1]):   #x=c[0] is tuple so grabs only pt (the [1]) Goes through all x indexes in c. #grab camera point, intersection point, compare distances, find closest.
                closest = x #Going through all rays to find smallest
        return closest[0].color #Taking Sphere0 return color. This part gave color to closest sphere.
    else:
        return False

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    w_interval = (max_x - min_x)/float(width)
    h_interval = (max_y - min_y)/float(height)  #To meet pixel width/height
                                                # , change increments. EX: -5 -> 5 in 100 pixels.
    print("P3")                                #add 0.1 every time.
    print("%d , %d") % (width,height)
    print("255")

    for i in range(width):
        for i2 in range(height):
            x = min_x + (i * w_interval)
            y = max_y - (i2 * h_interval)   #x & y values based off increments. NOTE: follows traditional x-y plane.

            dir = vector_math.vector_from_to(eye_point,data.Point(x,y,0))   #vector: camera to pixel point
            ray = data.Ray(eye_point,dir)   #generating ray in that direction.
            check = cast_ray(ray,sphere_list)

            if check is not False:

                max = 1.0  # Cap result at 1.0 to return max of 255 only.
                if check.r > max:
                    check.r = max
                if check.g > max:
                    check.g = max
                if check.b > max:
                    check.b = max

                print(int(check.r * 255)) # color
                print(int(check.g * 255))
                print(int(check.b * 255))

            else:
                return data.Color(1.0,1.0,1.0) #white










