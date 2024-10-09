arr = [3, 4, 6, -9, 10, 8, 9, 30]
arr.sort()

key1 = 10
key2 = 100

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

position1 = binary_search(arr, key1)
position2 = binary_search(arr, key2)

if position1 != -1:
    print(f"Element {key1} is found at position {position1}")
else:
    print(f"Element {key1} is not found")

if position2 != -1:
    print(f"Element {key2} is found at position {position2}")
else:
    print(f"Element {key2} is not found")
