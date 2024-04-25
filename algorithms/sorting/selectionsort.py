def selectionsort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        min_value = arr.pop(min_index)
        arr.insert(i, min_value)
    return arr
