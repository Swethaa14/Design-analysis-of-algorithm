def find_substrings(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return result

# Test cases
words1 = ["mass", "as", "hero", "superhero"]
print(find_substrings(words1))

words2 = ["leetcode", "et", "code"]
print(find_substrings(words2))

words3 = ["blue", "green", "bu"]
print(find_substrings(words3))
