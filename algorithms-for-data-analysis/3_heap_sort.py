import random

def heapify(arr, index, heap_size):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, heap_size)
    
    print(index, arr)

def create_heap(arr):
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(arr, i, heap_size)

def heap_sort(arr):
    print("Heapify")
    create_heap(arr)
    print("Sorting")
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


arr = [random.randint(0, 10) for _ in range(7)]
print(arr)
heap_sort(arr)
print(f"Sorted Arr: {arr}")