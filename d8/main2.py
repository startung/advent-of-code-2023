from enum import Enum
from math import lcm

elements = {}
class Directions(Enum):
    L = 0
    R = 1

with open('input', 'r') as f:
    instructions = f.readline()[:-1]
    f.readline() # skip empty line
    while element := f.readline():
        elements[element[:3]] = (element[7:10], element[12:15])

locations = [location for location in elements if location[2] == 'A']
counts = []
count = 0

for location in locations:
    found = False
    while not found:
        for instruction in instructions:
            count += 1
            location = elements[location][Directions[instruction].value]
            if location[2] == 'Z':
                counts.append(count)
                count = 0
                found = True
                break
print(lcm(*counts))