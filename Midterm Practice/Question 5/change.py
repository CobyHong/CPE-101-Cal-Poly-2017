def change_nums_only(string):
    result = ""
    for i in string:
        if i.isdigit():
            value = ord(i)
            change = chr(value + 2)
            result += change #the new value
        else:
            result += i #normal string addition
    return result
