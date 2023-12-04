import re

with open('input') as f:
    lines = f.readlines()

line_length = len(lines[0])

non_special_character = {'.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def surrounding(line, start, end):
    surrounding_characters = []
    if line != 0:
        surrounding_characters.extend(lines[line-1][max(0,start-1):min(line_length,end+1)])
    if start != 0:
        surrounding_characters.extend(lines[line][start-1])
    if end != line_length-1:
        surrounding_characters.extend(lines[line][end])
    if line != len(lines)-1:
        surrounding_characters.extend(lines[line+1][max(0,start-1):min(line_length,end+1)])
    return set(surrounding_characters)

total = 0
for line_number, line in enumerate(lines):
    iterator = re.finditer(r'\d+', line)
    for match in iterator:
        if surrounding(line_number, match.start(), match.end()) - non_special_character:
            total += int(match.group(0))
print(total)
