def find_kth_missing(arr, k):
    missing_count = 0
    current = 1
    index = 0

    while missing_count < k:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

arr1 = [2, 3, 4, 7, 11]
k1 = 5
print(find_kth_missing(arr1, k1))

arr2 = [1, 2, 3, 4]
k2 = 2
print(find_kth_missing(arr2, k2))
