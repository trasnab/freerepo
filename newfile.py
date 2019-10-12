def fibonacci(N):
    """Restituisce tutti i numeri di Fibonacci fino a N"""
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

print(list(fibonacci(100)))
