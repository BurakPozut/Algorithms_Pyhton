def unordered_list(arr, element):
    position = 0
    found = False

    while position < len(arr) and not found:
        if arr[position] == element:
            found = True
        else:
            position += 1

    return found


def ordered_list(arr, element):
    found = False

    for i in arr:
        if element > i:
            continue
        elif element < i:
            break
        else:
            found = True
    return found


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(unordered_list(array, 11))
