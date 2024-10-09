nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
answer1 = sum(1 for num in nums1 if num in nums2)
answer2 = sum(1 for num in nums2 if num in nums1)
result = [answer1, answer2]
print(result)
