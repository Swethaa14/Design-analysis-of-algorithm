a = [5, 7, 3, 4, 9, 12, 6, 2]

min_value = a[0]
max_value = a[0]

for i in a:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i

print(f"Min = {min_value}, Max = {max_value}")
