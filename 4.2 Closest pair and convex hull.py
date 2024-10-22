from math import sqrt

points = [(1, 2), (4, 5), (7, 8), (3, 1)]
d = lambda p1, p2: sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

min_distance = float('inf')
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = d(points[i], points[j])
        if dist < min_distance:
            min_distance = dist
            closest_pair = points[i], points[j]

print("Closest pair:", closest_pair)
print("Minimum distance:", min_distance)

points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
cross_product = lambda p1, p2, p3: (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

hull = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        all_on_one_side = True
        for k in range(len(points)):
            if k != i and k != j:
                if cross_product(points[i], points[j], points[k]) != 0:
                    all_on_one_side = False
                    break
        if all_on_one_side:
            hull.extend([points[i], points[j]])

hull = list(set(hull))  # Remove duplicates
print("Convex Hull:", hull)
