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

arr = [2,0,5,1,3,4,7,6,8,9]
print(f'Initial array: {arr}\n')

bubble_sort(arr)
