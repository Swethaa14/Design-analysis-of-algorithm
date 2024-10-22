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

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    
    medians = []
    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i+5])
        medians.append(group[len(group) // 2])
    
    pivot = median_of_medians(medians, len(medians) // 2)
    low, equal, high = partition(arr, pivot)
    
    if k <= len(low):
        return median_of_medians(low, k)
    elif k <= len(low) + len(equal):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(equal))

# Test cases
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 6
print(median_of_medians(arr1, k1))  # Output: 6

arr2 = [23, 17, 31, 44, 55, 21, 20, 18, 19, 27]
k2 = 5
print(median_of_medians(arr2, k2))  # Output: 21
