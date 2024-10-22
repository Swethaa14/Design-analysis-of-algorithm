import itertools

def total_cost(assignment, cost_matrix):
    return sum(cost_matrix[worker][task] for worker, task in enumerate(assignment))

def assignment_problem(cost_matrix):
    num_workers = len(cost_matrix)
    tasks = range(num_workers)
    min_cost = float('inf')
    best_assignment = []

    for assignment in itertools.permutations(tasks):
        current_cost = total_cost(assignment, cost_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = assignment

    return min_cost, best_assignment

test_cases = [
    [[3, 10, 7], [8, 5, 12], [4, 6, 9]],
    [[15, 9, 4], [8, 7, 18], [6, 12, 11]]
]

for i, cost_matrix in enumerate(test_cases, 1):
    min_cost, best_assignment = assignment_problem(cost_matrix)
    print(f"Test Case {i}:")
    print("Optimal Assignment:", [(f'worker {worker + 1}', f'task {task + 1}') for worker, task in enumerate(best_assignment)])
    print(f"Total Cost: {min_cost}\n")
