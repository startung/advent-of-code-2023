import re

with open('input') as f:
    lines = f.readlines()

line_length = len(lines[0])



def surrounding(line, position):
    surrounding_numbers = []
    if line != 0:
        iterator = re.finditer(r'\d+', lines[line-1])
        for match in iterator:
            if match.end() >= position and match.start() <= position+1:
                surrounding_numbers.append(int(match.group(0)))
    if position != 0 and lines[line][position-1].isdigit():
        surrounding_numbers.append(int(re.match("\d+", lines[line][position-1::-1]).group(0)[::-1]))
    if position != line_length-1 and lines[line][position+1].isdigit():
        surrounding_numbers.append(int(re.match("\d+", lines[line][position+1:]).group(0)))
    if line != len(lines)-1:
        iterator = re.finditer(r'\d+', lines[line+1])
        for match in iterator:
            if match.end() >= position and match.start() <= position+1:
                surrounding_numbers.append(int(match.group(0)))
    return 0 if len(surrounding_numbers) != 2 else surrounding_numbers[0] * surrounding_numbers[1]

total = 0

for line_number, line in enumerate(lines):
    total += sum([surrounding(line_number, idx) for idx, character in enumerate(line) if character == '*'])

print(total)
