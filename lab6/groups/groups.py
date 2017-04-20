def groups_of_3(list1):
    new_list = []
    for i in range(0, len(list1),3): #jumping by 3
        new_list.append(list1[i:i+3])
    return new_list
