def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):  # Arrange index numbers backwards
        # like if our list has 5 elements this piece of code will return us a [4,3,2,1]
        for k in range(n):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]

    print(arr)


arr = [5, 3, 2, 7, 8, 4, 9, 10]

bubble_sort(arr)
