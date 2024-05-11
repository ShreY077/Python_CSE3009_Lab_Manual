def fibonacci_series(n):
    fib_series = [0, 1]  # Initialize the Fibonacci series with first two terms

    # Generate Fibonacci series up to the nth term
    while fib_series[-1] + fib_series[-2] <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

# Test the function
fib_series = fibonacci_series(50)
print("Fibonacci series up to 50:", fib_series)
