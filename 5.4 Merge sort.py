comparison_count = 0

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global comparison_count
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

a = [12, 4, 78, 23, 45, 67, 89, 1]
sorted_a = merge_sort(a)
print(f"Sorted array: {sorted_a}")
print(f"Number of comparisons: {comparison_count}")
