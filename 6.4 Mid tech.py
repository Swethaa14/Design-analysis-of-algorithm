from itertools import combinations

def all_subset_sums(arr):
    sums = set()
    n = len(arr)
    for i in range(n + 1):
        for subset in combinations(arr, i):
            sums.add(sum(subset))
    return sums

def meet_in_the_middle(arr, exact_sum):
    n = len(arr)
    left_half = arr[:n//2]
    right_half = arr[n//2:]
    
    left_sums = all_subset_sums(left_half)
    right_sums = all_subset_sums(right_half)
    
    for left_sum in left_sums:
        if exact_sum - left_sum in right_sums:
            return True
    return False

# Test cases
arr1 = [1, 3, 9, 2, 7, 12]
exact_sum1 = 15
print(meet_in_the_middle(arr1, exact_sum1))  # Output: True

arr2 = [3, 34, 4, 12, 5, 2]
exact_sum2 = 15
print(meet_in_the_middle(arr2, exact_sum2))  # Output: True
