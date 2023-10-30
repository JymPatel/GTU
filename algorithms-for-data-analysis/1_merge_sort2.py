import time, random

def merge_sort(arr, start, end):
    if end - start <= 1:
        return arr[start:end]

    half = (end + start) // 2

    left = merge_sort(arr, start, half)
    right = merge_sort(arr, half, end)

    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    print(arr)
    return arr[start:end]

arr = [5, 6, 7, 1, 2, 8, 23, 0]
print(f'Initial array: {arr}\n')
time1 = time.time()
sorted_arr = merge_sort(arr, 0, len(arr))
time2 = time.time()
print(f'Sorted array: {sorted_arr}')
print(f"Time taken: {time2 - time1} seconds")

# arr = [random.randint(-100, 100) for _ in range(1000)]
# t1 = time.time()
# sorted_arr = merge_sort(arr, 0, len(arr))
# t2 = time.time()
# print(f"Time taken: {t2 - t1} seconds")
