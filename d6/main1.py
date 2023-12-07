with open("input", 'r') as f:
    times = list(filter(None, f.readline()[10:].strip().split(' ')))
    distances = list(filter(None, f.readline()[10:].strip().split(' ')))

def get_distances(time: int, distance_target: int) -> list[int]:
    distances = []
    for time_charging in range(time):
        distance_driving = time_charging * (time - time_charging)
        if distance_driving > distance_target:
            distances.append(distance_driving)
    return len(distances)

ways = [get_distances(int(time), int(distance)) for time, distance in zip(times, distances)]

ways_product = 1
for way in ways:
    ways_product *= way

print(ways_product)