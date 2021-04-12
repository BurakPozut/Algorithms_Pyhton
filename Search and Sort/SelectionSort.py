def selection_sort(arr):
    for fill_slot in range(len(arr)-1, 0, -1):  # Arrange index numbers backwards
        # like if our list has 5 elements this piece of code will return us a [4,3,2,1]
        position_of_max = 0
        for location in range(1, fill_slot+1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location
        arr[fill_slot], arr[position_of_max] = arr[position_of_max], arr[fill_slot]
        
    print(arr)


arr = [5, 42, 1, 55, 61, 10, 7, 8, 45]
selection_sort(arr)
