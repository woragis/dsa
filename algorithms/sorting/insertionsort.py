def insertionsort(arr):
    for i in range(len(arr)):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)
    return arr
