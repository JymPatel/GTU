def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'Pass {i+1}: {arr}')
    return arr

arr = [2,5,1,3,4,7,6,8,9,0]
print(f'Initial array: {arr}\n')

selection_sort(arr)
