def str_rot_13(x):
    result = ""
    for i in x:
        chr_to_num = ord(i) #convert letter to number value
        if ord('a') <= chr_to_num <= ord('z'): #Lowercase variables
            if chr_to_num > ord('m'):
                chr_to_num -= 13
            else:
                chr_to_num += 13
        elif ord('A') <= chr_to_num <= ord('Z'): #Uppcase variables
            if chr_to_num > ord('M'):
                chr_to_num -= 13
            else:
                chr_to_num += 13

        result += chr(chr_to_num) #Stacking results and convert back to characters

    return result

def str_translate_101(x,old,new):
    result = ""
    for i in x:
        if i == old:
            result += new
        else:
            result += i
    return result








