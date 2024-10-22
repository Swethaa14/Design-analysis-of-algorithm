def strassen_multiply(A, B):
    # Elements of matrix A
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    
    # Elements of matrix B
    e, f = B[0][0], B[0][1]
    g, h = B[1][0], B[1][1]
    
    # Strassen's seven products
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)
    
    # Calculating the elements of the resulting matrix C
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7
    
    return [[c11, c12], [c21, c22]]

# Test case 1
A1 = [[1, 7], [3, 5]]
B1 = [[6, 8], [4, 2]]
C1 = strassen_multiply(A1, B1)
for row in C1:
    print(row)

# Expected Output:
# [34, 22]
# [38, 34]
