# Square root calculation using Newton-Raphson method

def square_root(number, tolerance=1e-6):
    """
    Calculate the square root of a number using the Newton-Raphson method.

    Formula:
        x_(n+1) = 0.5 * (x_n + number / x_n)
    """
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    # Initial guess
    x = number / 2 if number > 1 else 1.0

    # Iteratively improve the estimate
    while True:
        root = 0.5 * (x + number / x)
        if abs(root - x) < tolerance:
            break
        x = root

    return root


# Example usage
if __name__ == "__main__":
    num = float(input("Enter a number to find its square root: "))
    result = square_root(num)
    print(f"The square root of {num} is approximately {result:.6f}")
