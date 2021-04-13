def quick_sort(array):
    quick_sort_rec(array, 0, len(array)-1)
    print(array)


def quick_sort_rec(array, first, last):
    if first < last:
        split_point = partition(array, first, last)
        quick_sort_rec(array, first, split_point-1)
        quick_sort_rec(array, split_point+1, last)


def partition(array, first, last):
    pivot_value = array[first]
    left_mark = first+1
    right_mark = last

    while True:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark +=1

        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -=1
        if right_mark < left_mark:
            break
        else:
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]

    array[first], array[right_mark] = array[right_mark], array[first]
    return right_mark


array = [2, 55, 14, 23, 6, 87, 12, 5, 47]
quick_sort(array)
