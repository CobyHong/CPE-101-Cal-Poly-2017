def less_than_5(list):
    list_str = []
    for i in range(len(list)):
        if len(list[i]) < 5:
            list_str.append(list[i])
            result = len(list_str)
    return result