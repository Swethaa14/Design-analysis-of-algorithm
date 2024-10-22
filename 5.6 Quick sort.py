def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"Pivot: {pivot}")
    print(f"Left: {left}")
    print(f"Right: {right}")
    
    return quick_sort(left) + [pivot] + quick_sort([x for x in arr if x == pivot][1:]) + quick_sort(right)

a = [19, 72, 35, 46, 58, 91, 22, 31]
sorted_a = quick_sort(a)
print(f"Sorted array: {sorted_a}")
