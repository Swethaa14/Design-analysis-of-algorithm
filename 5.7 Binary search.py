def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == key:
            print(f"Number of comparisons: {comparisons}")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    print(f"Number of comparisons: {comparisons}")
    return -1

a = [5, 10, 15, 20, 25, 30, 35, 40, 45]
search_key = 20
result = binary_search(a, search_key)

if result != -1:
    print(f"Element {search_key} found at index: {result}")
else:
    print(f"Element {search_key} not found in the array.")
