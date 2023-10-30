import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

my_list = [3, 6, 8, 10, 1, 2, 1]
t1 = time.time()
sorted_list = quick_sort(my_list)
print(f"Sorted Array: {sorted_list}")
print(f"Time taken: {time.time() - t1}")
