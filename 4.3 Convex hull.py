points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]

cross_product = lambda p1, p2, p3: (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull_brute_force(points):
    hull = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            left_side = True
            right_side = True
            for k in range(len(points)):
                if k != i and k != j:
                    cp = cross_product(points[i], points[j], points[k])
                    if cp < 0:
                        left_side = False
                    if cp > 0:
                        right_side = False
            if left_side or right_side:
                hull.extend([points[i], points[j]])

    hull = list(set(hull))
    hull.sort(key=lambda p: (p[0], p[1]))

    return hull

hull = convex_hull_brute_force(points)

print("Convex Hull:", hull)
