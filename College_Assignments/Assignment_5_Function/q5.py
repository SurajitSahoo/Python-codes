def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series


num_terms = 10
print(f"Fibonacci series up to {num_terms} terms: {fibonacci(num_terms)}")
