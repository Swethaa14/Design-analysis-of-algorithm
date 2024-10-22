from collections import defaultdict

def four_sum_count(A, B, C, D):
    # Dictionary to hold the sums of A and B
    sum_ab = defaultdict(int)

    # Compute all possible sums of elements from A and B
    for a in A:
        for b in B:
            sum_ab[a + b] += 1

    count = 0
    # Compute sums of elements from C and D and find complements in sum_ab
    for c in C:
        for d in D:
            count += sum_ab[-(c + d)]

    return count

# Test cases
A1 = [1, 2]
B1 = [-2, -1]
C1 = [-1, 2]
D1 = [0, 2]
print(four_sum_count(A1, B1, C1, D1))  # Output: 2

A2 = [0]
B2 = [0]
C2 = [0]
D2 = [0]
print(four_sum_count(A2, B2, C2, D2))  # Output: 1
5
