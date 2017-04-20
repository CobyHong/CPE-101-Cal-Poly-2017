def reverse_triplet(list):
    result = []
    for i in range(len(list)-1, -1, -1):
        if list[i] + list[i-1] + list[i-2] == list[i] * 3:
            result.append(list[i])
            result.append(i)
            break
    return result

