numbers = list(range(1,11))
squares = [n * n for n in numbers if n % 2 == 0]
odds = [ n for n in numbers if n % 2 != 0]
def generate_data(n):
    return [i * 2 for i in range(1, n)]
data = generate_data(100)
filtered = [x for x in data if x % 10 == 0]