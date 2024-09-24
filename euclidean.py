points = [(1, 3), (4, 5), (7, 8), (4, 1), (3, 5)]

# Function to calculate the Euclidean distance between two points
def euclideanDistance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# List to store distances
distances = []

# Calculate distances between all point pairs
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Find and print the minimum distance
min_distance = min(distances)
print(min_distance)
