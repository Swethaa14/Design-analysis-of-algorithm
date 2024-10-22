def karatsuba(x, y):
    if x < 10 or y < 10:  # Base case for small numbers
        return x * y

    n = max(len(str(x)), len(str(y)))  # Length of the larger number
    half = n // 2  # Midpoint for splitting the numbers
    
    # Split x and y
    x_high, x_low = divmod(x, 10**half)
    y_high, y_low = divmod(y, 10**half)
    
    # Recursive calls
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)
    
    # Karatsuba formula
    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

# Test Case
x = 1234
y = 5678
z = karatsuba(x, y)
print(z)  # Expected Output: 7016652
