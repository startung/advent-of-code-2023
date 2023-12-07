with open("input", 'r') as f:
    time = int(f.readline()[10:].strip().replace(' ', ''))
    distance = int(f.readline()[10:].strip().replace(' ', ''))

def number_winning(time: int, distance_target: int) -> list[int]:
    distances = []
    for time_charging in range(time):
        distance_driving = time_charging * (time - time_charging)
        if distance_driving > distance_target:
            distances.append(distance_driving)
    return len(distances)

print(number_winning(time, distance))