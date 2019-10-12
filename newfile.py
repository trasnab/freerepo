def fibonacci(N):
    """Restituisce tutti i numeri di Fibonacci fino a N"""
    a, b = 0, 1
    while b <= N:
        yield b
        a, b = b, a + b

fib = (list(fibonacci(100)))

print(fib)
