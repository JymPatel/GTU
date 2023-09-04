import time, sys

sys.setrecursionlimit(100000)
def recursive_factorial(n):
    if n <= 1:
        return 1
    
    return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

n = int(input("n? "))

recursive_time = time.time()
factorial = recursive_factorial(n)
print(f"Recursive: {time.time() - recursive_time}")

iterative_time = time.time()
factorial = iterative_factorial(n)
print(f"Iterative: {time.time() - iterative_time}")
