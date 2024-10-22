from itertools import combinations

def all_subset_sums(arr):
    sums = []
    n = len(arr)
    for i in range(n + 1):
        for subset in combinations(arr, i):
            sums.append(sum(subset))
    return sorted(sums)

def meet_in_the_middle(arr, target_sum):
    n = len(arr)
    left_half = arr[:n//2]
    right_half = arr[n//2:]
    
    left_sums = all_subset_sums(left_half)
    right_sums = all_subset_sums(right_half)
    
    closest_sum = float('-inf')
    
    i, j = 0, len(right_sums) - 1
    while i < len(left_sums) and j >= 0:
        current_sum = left_sums[i] + right_sums[j]
        
        if abs(target_sum - current_sum) < abs(target_sum - closest_sum):
            closest_sum = current_sum
        
        if current_sum < target_sum:
            i += 1
        else:
            j -= 1
            
    return closest_sum

# Test cases
set1 = [45, 34, 4, 12, 5, 2]
target1 = 42
print(meet_in_the_middle(set1, target1))  # Closest sum to 42

set2 = [1, 3, 2, 7, 4, 6]
target2 = 10
print(meet_in_the_middle(set2, target2))  # Closest sum to 10
