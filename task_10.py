import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end-start:.4f} seconds')
        return result
    return wrapper
@timer
def heavy_computation(n):
    return sum(i * i for i in range(n))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = list(map(lambda x: x ** x, numbers))
filtered = list(filter(lambda x: x > 10, squares))
print("squared:", squares)
print("filtered:", filtered)