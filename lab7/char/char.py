
def is_lower_101(x):
    #Test if everything in string is lowercase.
    for i in x:
        if 'a' <= x <= 'z':
            return True
        else:
            return False

def char_rot_13(x):
    #Number value of letter scaled 13 up.
    if is_lower_101(x):
    #Lowercase adds 13
        for i in x:
            lower_rot = ord(x) + 13
        return chr(lower_rot)
    else:
    #Uppercase minus 13
        for i in x:
            higher_rot = ord(x) - 13
        return chr(higher_rot)
