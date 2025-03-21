def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0  # Base case: First Fibonacci number is 0
    elif n == 2:
        return 1  # Base case: Second Fibonacci number is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example usage
num = 6
print(f"Fibonacci number at position {num} is {fibonacci(num)}")
