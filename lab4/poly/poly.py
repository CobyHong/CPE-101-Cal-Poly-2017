import math

def poly_add2(poly1,poly2):
    poly_x = poly1[0] + poly2[0]
    poly_y = poly1[1] + poly2[1]
    poly_z = poly1[2] + poly2[2]
    return [poly_x,poly_y,poly_z]

def poly_mult2(poly1,poly2):
#Poly1--> (A1X^2+B1X+C1)*(A2X^2+B2X+C2) <--Poly2
    poly_a1 = poly1[0] * poly2[0]   #Distribution of A1 to all of other polynomial 2
    poly_a2 = poly1[0] * poly2[1]
    poly_a3 = poly1[0] * poly2[2]

    poly_b1 = poly1[1] * poly2[0]   #Distribution of B1 to all of other polynomial 2
    poly_b2 = poly1[1] * poly2[1]
    poly_b3 = poly1[1] * poly2[2]

    poly_c1 = poly1[2] * poly2[0]   #Distribution of C1 of all of other polynomal 2
    poly_c2 = poly1[2] * poly2[1]
    poly_c3 = poly1[2] * poly2[2]

    return [poly_c3,(poly_b3 + poly_c2),(poly_a3 + poly_b2 + poly_c1),(poly_a2 + poly_b1), poly_a1] #[Constant,X^1,X^2,X^3,X^4] Least to Greatest Exponenet
