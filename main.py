def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def print_recurrence_relation():
    print("Recurrence relation for the fibonacci function:")
    print("T(n) = T(n-1) + T(n-2) + 0(1)")
    print("Bases cases:")
    print("T(0) = 0(1)")
    print("T(1) = 0(1)")

if __name__ == "__main__":
    # Example usage
    n = 5
    result = fibonacci(n)
    print(f"Fibonacci of {n}: {result}")

    # Print recurrence relation
    print_recurrence_relation()