import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the Haversine distance between two points on the Earth.
    :param lat1: Latitude of point 1
    :param lon1: Longitude of point 1
    :param lat2: Latitude of point 2
    :param lon2: Longitude of point 2
    :return: Distance in kilometers
    """
    R = 6371.0  # Earth's radius in kilometers

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def nearest_neighbor(start_point, distribution_points):
    """
    Find the nearest neighbor for a given start point from a list of distribution points.
    :param start_point: A tuple (latitude, longitude) for the starting point
    :param distribution_points: A list of tuples [(lat1, lon1), (lat2, lon2), ...]
    :return: The nearest distribution point and its distance
    """
    closest_point = None
    min_distance = float('inf')

    for point in distribution_points:
        distance = haversine(start_point[0], start_point[1], point[0], point[1])
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    return closest_point, min_distance

# Example usage:
if __name__ == "__main__":
    start = (34.0522, -118.2437)  # Los Angeles, CA
    points = [
        (34.0407, -118.2468),  # Nearby point
        (34.1478, -118.1445),  # Another nearby point
        (36.7783, -119.4179)   # Far away point
    ]

    nearest, distance = nearest_neighbor(start, points)
    print(f"The nearest point is at {nearest} with a distance of {distance:.2f} km")
