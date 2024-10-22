import heapq

def k_closest(points, k):
    # Create a max heap for the k closest points
    max_heap = []
    
    for (x, y) in points:
        distance = x**2 + y**2
        # Push the negative distance to simulate max heap using min heap
        heapq.heappush(max_heap, (-distance, [x, y]))
        # Keep only the k closest points in the heap
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    # Extract the points from the heap
    return [point for (_, point) in max_heap]

# Test cases
points1 = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k1 = 2
print(k_closest(points1, k1))  # Output: [[-2, 2], [0, 1]]

points2 = [[1, 3], [-2, 2]]
k2 = 1
print(k_closest(points2, k2))  # Output: [[-2, 2]]

points3 = [[3, 3], [5, -1], [-2, 4]]
k3 = 2
print(k_closest(points3, k3))  # Output: [[3, 3], [-2, 4]]
