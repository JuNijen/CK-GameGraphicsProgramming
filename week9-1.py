def sumList(data):
    sum = 0

    for i in range (0, len(data), 1):
        sum += data[i]
    return sum


num_list = [1, 11, 21, 31, 41, 51]
print(sumList(num_list))