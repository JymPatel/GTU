import time, random

def insertion_sort(arr):
    for i in range(len(arr)):
        num = arr[i]
        j = i
        while j > 0:
            if arr[j - 1] > num:
                arr[j] = arr[j - 1]
            else:
                break
            j -= 1
        arr[j] = num
        print(f"Pass {i + 1}: {arr}")
    return arr


arr = [random.randint(-100, 100) for _ in range(1000)]
print(f'Initial array: {arr}\n')

t1 = time.time()
insertion_sort(arr)
print(f"Time taken: {time.time() - t1} seconds")