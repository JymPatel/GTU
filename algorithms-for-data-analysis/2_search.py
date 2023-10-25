import random
import time

def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return -1

arr = [random.randint(-1000, 10000) for _ in range(5000)]
arr.sort()

print(arr)
t1 = time.time()
linear_index = linear_search(arr, 500)
t2 = time.time()
binary_index = binary_search(arr, 500)
t3 = time.time()

print(f"Linear search found at index {linear_index} in {t2 - t1} seconds")
print(f"Binary search found at index {binary_index} in {t3 - t2} seconds")
