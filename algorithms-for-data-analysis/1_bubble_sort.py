import time, random

def bubble_sort(arr):
    flag = False
    for i in range(len(arr)):
        if flag:
            break
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                flag = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'Pass {i+1}: {arr}')
    return arr

arr = [random.randint(-100, 100) for _ in range(1000)]
print(f'Initial array: {arr}\n')

t1 = time.time()
bubble_sort(arr)
print(f"Time taken: {time.time() - t1} seconds")