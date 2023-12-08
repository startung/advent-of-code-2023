from enum import Enum

elements = {}
class Directions(Enum):
    L = 0
    R = 1

with open('input', 'r') as f:
    instructions = f.readline()[:-1]
    f.readline() # skip empty line
    while element := f.readline():
        elements[element[:3]] = (element[7:10], element[12:15])

location = 'AAA'
count = 0
while True:
    for instruction in instructions:
        count += 1
        location = elements[location][Directions[instruction].value]
        if location == 'ZZZ':
            print(count)
            quit()