def binary_search(arr, item):   # We take take the middle element of the array and than check if its bigger or smaller
    # than out element, if its bigger than out element than we eliminate small part of the list
    first = 0
    last = len(arr)
    found = False

    while first <= last and not found:
        middle = (first+last)//2

        if arr[middle] == item:
            return True
        elif arr[middle] < item:
            first = middle+1
        else:
            last = middle-1
    return found


def rec_binary(arr, item):  # Same program but with recursion

    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == item:
            return True
        else:
            if arr[mid] > item:
                return rec_binary(arr[:mid], item)
            else:
                return rec_binary(arr[mid+1:], item)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 40, 55, 78, 98]
print(rec_binary(arr, 5))
