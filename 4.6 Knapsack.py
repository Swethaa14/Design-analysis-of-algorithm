from itertools import combinations

items = [0, 1, 2]  # Modify this list for different test cases
weights = [2, 3, 1]
values = [4, 5, 3]
capacity = 4

def total_value(selected_items, values):
    return sum(values[i] for i in selected_items)

def is_feasible(selected_items, weights, capacity):
    return sum(weights[i] for i in selected_items) <= capacity

best_value = 0
best_combination = []

for r in range(len(items) + 1):
    for combination in combinations(items, r):
        if is_feasible(combination, weights, capacity):
            value = total_value(combination, values)
            if value > best_value:
                best_value = value
                best_combination = combination

print(f"Optimal Selection: {list(best_combination)}")
print(f"Total Value: {best_value}")
