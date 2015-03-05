def factorial(n):
    total, index = 1, 1
    while index <= n:
        total *= index
        index += 1
    return total
