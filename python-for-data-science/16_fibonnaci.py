def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    arr = fibonacci(n - 1)
    arr.append(arr[-1] + arr[-2])
    return arr

n = 5
print(f"fibonnaci of {n} digits: {fibonacci(n)}")