import random

arr = []

for i in range(20):
    arr.append(random.randint(1, 1000))

max_value = max(arr)
max_digits = 0
while max_value > 0:
    max_value = max_value // 10
    max_digits += 1

def radix_sort(arr, key):
    new_arr = []
    print(f"Key: {key}")
    for i in range(10):
        print(i, arr)
        for element in arr:
            if ((element % key) / key) * 10 == i:
                new_arr.append(element)
                print(element)
    
    print(new_arr)
    return new_arr

for i in range(1, max_digits + 1):
    arr = radix_sort(arr, 10 ** i)
