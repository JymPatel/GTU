def merge_sort(arr):
    if len(arr) == 1:
        return arr
    half = len(arr) // 2
    
    left, right = merge_sort(arr[:half]), merge_sort(arr[half:])
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    for i in range(i, len(left)):
        arr[k] = left[i]
        k += 1
    for j in range(j, len(right)):
        arr[k] = right[j]
        k += 1
    
    print(arr)
    return arr


arr = [2,5,1,3,4,7,6,8,9,0]
print(f'Initial array: {arr}\n')

merge_sort(arr)
