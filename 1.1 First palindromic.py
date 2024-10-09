words = ["abc","car","ada","racecar","cool"]

# Loop through each word and check if it is a palindrome
result = ""
for word in words:
    if word == word[::-1]:
        result = word
        break

print(result)
