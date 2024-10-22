def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        print(f"Current low: {low}, Current high: {high}, Mid-point: {mid}, Mid-value: {arr[mid]}")
        
        if arr[mid] == key:
            print(f"Number of comparisons: {comparisons}")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    print(f"Number of comparisons: {comparisons}")
    return -1

# Test the Binary Search
a = [3, 9, 14, 19, 25, 31, 42, 47, 53]
search_key = 31
result = binary_search(a, search_key)

if result != -1:
    print(f"Element {search_key} found at index: {result}")
else:
    print(f"Element {search_key} not found in the array.")
