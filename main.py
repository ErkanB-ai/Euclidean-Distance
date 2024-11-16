import math

# Öklid mesafesi hesaplamak için bir fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafeleri hesaplayıp saklamak
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

print(f"Tüm noktalar arasındaki mesafeler: {distances}")
print(f"En kısa mesafe: {min_distance}")