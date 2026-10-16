"""
Week 3 - Fibonacci Series
Generates Fibonacci series up to n terms / n-th term.
"""

def fibonacci_series(n_terms):
    """Return list of first n_terms of Fibonacci series using iteration."""
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    series = [0, 1]
    for _ in range(2, n_terms):
        series.append(series[-1] + series[-2])
    return series


def fibonacci_nth(n):
    """Return nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1) using iteration."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursive(n):
    """Return nth Fibonacci number using recursion (for learning/demo)."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    print("=== Week 3: Fibonacci Series ===")
    try:
        n = int(input("Enter number of terms (e.g. 10): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        series = fibonacci_series(n)
        print(f"\nFibonacci series ({n} terms):")
        print(", ".join(map(str, series)))

        print(f"\nThe {n}th term (1-indexed) is: {series[-1]}")
        print(f"fib({n-1}) 0-indexed = {fibonacci_nth(n-1)}")

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
