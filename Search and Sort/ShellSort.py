def shell_sort(array):
    sub_list_count = len(array)//2

    while sub_list_count > 0:
        for start in range(sub_list_count):
            gap_insertion_sort(array, start, sub_list_count)
        sub_list_count = sub_list_count//2
    print(array)


def gap_insertion_sort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        current_val = array[i]
        position = i

        while position >= gap and array[position-gap] > current_val:
            array[position] = array[position-gap]
            position = position-gap
        array[position] = current_val


array = [4, 31, 72, 55, 1, 5]
shell_sort(array)
