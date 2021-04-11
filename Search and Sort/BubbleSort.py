def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1): # Arrange everything backwards except the last element because that last '-1'
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp

    print(arr)


arr = [5,3,2,7,8,4,9,10]

bubble_sort(arr)