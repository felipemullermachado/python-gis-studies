# 1. Create a list of tuples, each representing the coordinates (latitude, longitude)
# of different cities you have visited.

cities = [
    [-28.327867, -49.065493],
    [-27.597269, -48.553667],
    [-26.895915, -48.717506],
    [-26.815743, -49.089441]
]

# 2. Calculate the centroid of these coordinates.
centroid_lat = sum(city[0] for city in cities) / len(cities)
centroid_lon = sum(city[1] for city in cities) / len(cities)

# 3. Create a dictionary to store the centroid’s latitude and longitude.
centroid = {
    "latitude": centroid_lat,
    "longitude": centroid_lon,
}
print(centroid["latitude"], centroid["longitude"])
