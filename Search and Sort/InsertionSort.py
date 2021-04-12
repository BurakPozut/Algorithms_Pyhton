def insertion_sort(array):
    for i in range(1, len(array)):  # range func. goes 1 to n-1
        current_val = array[i]
        position = i

        while position > 0 and array[position-1] > current_val:
            array[position] = array[position-1]
            position -= 1
        array[position] = current_val
    print(array)


array = [1, 2, 55, 4, 6, 47, 89, 65, 6]

insertion_sort(array)
