nums = [1, 2, 1]
result = 0
for i in range(len(nums)):
    distinct_count = 0
    seen = []
    for j in range(i, len(nums)):
        if nums[j] not in seen:
            seen.append(nums[j])
            distinct_count += 1
        result += distinct_count ** 2

print(result)
