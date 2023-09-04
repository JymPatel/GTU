import time, random

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'Pass {i+1}: {arr}')
    return arr


arr = [random.randint(-100, 100) for _ in range(1000)]
print(f'Initial array: {arr}\n')

t1 = time.time()
selection_sort(arr)
print(f"Time taken: {time.time() - t1} seconds")
