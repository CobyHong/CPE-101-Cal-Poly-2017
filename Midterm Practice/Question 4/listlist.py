def diagnol(list):
    result = []
    for i in range(len(list)):
        result.append(list[i][0])
        result.append(list[i+1][1])
        result.append(list[i+2][2])
        break
    return result