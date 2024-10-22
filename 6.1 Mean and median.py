def partition(arr, pivot):
    low, high, equal = [], [], []
    for num in arr:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            equal.append(num)
    return low, equal, high

def select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    
    medians = []
    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i+5])
        medians.append(group[len(group) // 2])
    
    pivot = select(medians, len(medians) // 2)
    low, equal, high = partition(arr, pivot)
    
    if k <= len(low):
        return select(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return select(high, k - len(low) - len(equal))

# Test cases
arr1 = [12, 3, 5, 7, 19]
k1 = 2
print(select(arr1, k1))  # Expected Output: 5

arr2 = [12, 3, 5, 7, 4, 19, 26]
k2 = 3
print(select(arr2, k2))  # Expected Output: 5

arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 6
print(select(arr3, k3))  # Expected Output: 6
